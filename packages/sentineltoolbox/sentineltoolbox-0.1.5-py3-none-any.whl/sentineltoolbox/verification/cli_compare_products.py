import logging
import sys
from io import TextIOWrapper
from typing import Any, Dict, TextIO

import click
import xarray as xr

from sentineltoolbox.readers.datatree_subset import filter_flags
from sentineltoolbox.readers.open_datatree import open_datatree
from sentineltoolbox.verification.compare import (
    _get_failed_formatted_string_flags,
    _get_failed_formatted_string_vars,
    _get_passed_formatted_string_flags,
    bitwise_statistics,
    parse_cmp_vars,
    product_exists,
    sort_datatree,
    variables_statistics,
)
from sentineltoolbox.verification.logger import (
    get_failed_logger,
    get_logger,
    get_passed_logger,
)


@click.command()
@click.argument("reference", type=str, nargs=1, required=True)
@click.argument("actual", type=str, nargs=1, required=True)
@click.option(
    "--cmp-vars",
    type=str,
    help="Compare only specific variables, defined as: path/to/var_ref:path/to/var_new,... ",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    default=False,
    show_default=True,
    help="increased verbosity",
)
@click.option(
    "--relative",
    is_flag=True,
    default=False,
    show_default=True,
    help="Compute relative error",
)
@click.option(
    "--threshold",
    required=False,
    type=float,
    default=1.0e-6,
    show_default=True,
    help="Error Threshold defining the PASSED/FAILED result",
)
@click.option(
    "--flags-only",
    required=False,
    is_flag=True,
    default=False,
    show_default=True,
    help="Compute comparison only for flags/masks variables",
)
@click.option(
    "-s",
    "--secret",
    required=False,
    show_default=True,
    help="Secret alias if available extracted from env. variable S3_SECRETS_JSON_BASE64 or in /home/.eopf/secrets.json",
)
@click.option("-o", "--output", required=False, help="output file")
def compare(
    reference: str,
    actual: str,
    cmp_vars: str,
    verbose: bool,
    relative: bool,
    threshold: float,
    flags_only: bool,
    secret: str,
    output: str,
    **kwargs: Any,
) -> None:
    """CLI tool to compare two products Zarr or SAFE

    Parameters
    ----------
    reference: Path
        Reference product path
    actual: Path
        New product path
    verbose: bool
        2-level of verbosity (INFO or DEBUG)
    relative: bool
        Compute relative or absolute error, default is True
    threshold
        Threshold to determine wheter the comparison is PASSED or FAILED
    """
    # Initialize stream
    stream: TextIOWrapper | TextIO
    if output:
        stream = open(output, mode="w")
    else:
        stream = sys.stderr

    # Initialize logging
    level = logging.INFO
    if verbose:
        level = logging.DEBUG
    logger = get_logger("compare", level=level, stream=stream)
    logger.setLevel(level)

    passed_logger = get_passed_logger("passed", stream=stream)
    failed_logger = get_failed_logger("failed", stream=stream)

    # Check input products
    if not product_exists(reference, secret=secret):
        logger.error(f"{reference} cannot be found.")
        exit(1)
    if not product_exists(actual, secret=secret):
        logger.error(f"{actual} cannot be found.")
        exit(1)
    logger.info(
        f"Compare the new product {actual} to the reference product {reference}",
    )

    # Check if specific variables
    if cmp_vars:
        list_ref_new_prods = parse_cmp_vars(reference, actual, cmp_vars)
    else:
        list_ref_new_prods = [
            (reference, actual),
        ]

    kwargs["decode_times"] = False
    if secret:
        kwargs["secret_alias"] = secret
    # Loop over input products
    for ref_prod, new_prod in list_ref_new_prods:
        # Open reference product
        # dt_ref = open_datatree(ref_prod, fs_copy=True, decode_times=False)
        dt_ref = open_datatree(ref_prod, **kwargs)
        dt_ref.name = "ref"
        logger.debug(dt_ref)

        # Open new product
        # dt_new = open_datatree(new_prod, fs_copy=True, decode_times=False)
        dt_new = open_datatree(new_prod, **kwargs)
        dt_new.name = "new"
        logger.debug(dt_new)

        # Sort datatree
        dt_ref = sort_datatree(dt_ref)
        dt_new = sort_datatree(dt_new)

        # Check if datatrees are isomorphic
        if not dt_new.isomorphic(dt_ref):
            logger.error("Reference and new products are not isomorphic")
            logger.error("Comparison fails")
            return

        # dt_ref = drop_duplicates(dt_ref)
        # dt_new = drop_duplicates(dt_new)
        # dt_new = encode_time_datatree(dt_new)
        # dt_ref = encode_time_datatree(dt_ref)

        # Variable statistics
        if not flags_only:
            if relative:
                dt_ref_tmp = dt_ref.where(dt_ref != 0)
                dt_new_tmp = dt_new.where(dt_ref != 0)
                err = (dt_new_tmp - dt_ref_tmp) / dt_ref_tmp
            else:
                err = dt_new - dt_ref  # type: ignore

            results: Dict[str, Any] = variables_statistics(err, threshold)

            logger.info("-- Verification of variables")
            for name, val in results.items():
                if all(v < threshold for v in val[:-2]):
                    passed_logger.info(f"{name}")
                else:
                    failed_logger.info(
                        _get_failed_formatted_string_vars(
                            name,
                            val,
                            threshold,
                            relative=relative,
                        ),
                    )

        # Flags statistics
        flags_ref = filter_flags(dt_ref)
        flags_new = filter_flags(dt_new)

        try:
            with xr.set_options(keep_attrs=True):
                err_flags = flags_ref ^ flags_new
        except TypeError:
            pass
        else:
            res: Dict[str, xr.Dataset] = bitwise_statistics(err_flags)
            eps = 100.0 * (1.0 - threshold)
            logger.info(f"-- Verification of flags: threshold = {eps}%")
            for name, ds in res.items():
                # ds_outlier = ds.where(ds.equal_percentage < eps, other=-1, drop=True)
                for bit in ds.index.data:
                    if ds.equal_percentage[bit] < eps:
                        failed_logger.info(
                            _get_failed_formatted_string_flags(name, ds, bit, eps),
                        )
                    else:
                        passed_logger.info(
                            _get_passed_formatted_string_flags(name, ds, bit),
                        )

        logger.info("Exiting compare")

    if output:
        stream.close()

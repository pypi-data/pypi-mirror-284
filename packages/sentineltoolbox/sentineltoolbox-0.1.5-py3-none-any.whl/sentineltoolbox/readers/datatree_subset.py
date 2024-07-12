import datatree
import xarray as xr


@datatree.map_over_subtree
def filter_flags(ds: xr.Dataset) -> xr.Dataset:
    """Filter only flags variable while preserving the whole structure
    Following the CF convention, flag variables are filtered based on the presence of "flag_masks" attribute

    Parameters
    ----------
    ds
        input xarray.Dataset or datatree.DataTree

    Returns
    -------
        xarray.Dataset or datatree.DataTree
    """
    return ds.filter_by_attrs(flag_masks=lambda v: v is not None)

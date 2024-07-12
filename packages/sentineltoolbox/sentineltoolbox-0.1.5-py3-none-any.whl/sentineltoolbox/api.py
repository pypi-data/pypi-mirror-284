# all function are loaded in api module instead of in sentineltoolbox/__init__.py
# to avoid to load all dependencies each time.
# For example, pip loads sentineltoolbox to extract __version__ information.
# In this case, we don't want to load all sub packages and associated dependencies

from .adfs import check_adfs
from .attributes import AttributeHandler
from .configuration import get_config
from .converters import convert_to_datatree
from .datatree_utils import DataTreeHandler, patch_datatree
from .filesystem_utils import get_fsspec_filesystem
from .flags import create_flag_array, get_flag, update_flag
from .models.credentials import S3BucketCredentials, map_secret_aliases
from .models.filename_generator import (
    AdfFileNameGenerator,
    ProductFileNameGenerator,
    detect_filename_pattern,
)
from .readers.open_dataset import load_dataset, open_dataset
from .readers.open_datatree import load_datatree, open_datatree
from .readers.open_json import open_json
from .readers.open_metadata import load_metadata
from .typedefs import Adf

__all__: list[str] = [
    "Adf",
    "AdfFileNameGenerator",
    "AttributeHandler",
    "DataTreeHandler",
    "ProductFileNameGenerator",
    "S3BucketCredentials",
    "check_adfs",
    "convert_to_datatree",
    "create_flag_array",
    "detect_filename_pattern",
    "get_config",
    "get_flag",
    "get_fsspec_filesystem",
    "load_dataset",
    "load_datatree",
    "load_metadata",
    "map_secret_aliases",
    "open_dataset",
    "open_datatree",
    "open_json",
    "patch_datatree",
    "update_flag",
]

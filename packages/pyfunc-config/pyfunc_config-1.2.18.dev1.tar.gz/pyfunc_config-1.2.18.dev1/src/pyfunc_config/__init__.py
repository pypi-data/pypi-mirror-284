# Auto-generated __init__.py

# Version of the pyfunc2 package
#from pathlib import Path

# you can use os.path and open() as well
#__version__ = Path(__file__).parent.joinpath("VERSION").read_text()

# Import necessary modules and functions here
from get_email_path import get_email_path
from get_config import get_config
from ftp_update import ftp_update
from ftp_download import ftp_download
from get_ftp_path import get_ftp_path

# Public API of the package
__all__ = [get_ftp_path, get_email_path, get_config, ftp_update, ftp_download]

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pyfunc_config")
except PackageNotFoundError:
    # package is not installed
    pass
__version__ = '1.2.18'

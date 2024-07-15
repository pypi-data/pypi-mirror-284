# Auto-generated __init__.py for pyfunc_config package

# Import necessary modules
from . import get_ftp_path
from . import get_email_path
from . import get_config
from . import ftp_update
from . import ftp_download

# Public API of the package
__all__ = ['get_ftp_path', 'get_email_path', 'get_config', 'ftp_update', 'ftp_download']

# Version checking
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pyfunc_config")
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

# You can add any initialization code here if needed

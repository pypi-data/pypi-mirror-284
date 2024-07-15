from . import ftp_download
from . import get_ftp_path

def ftp_update(ftps, storage_root, limit=3):
    for ftp in ftps:
        data_path = get_ftp_path(ftp["target"], storage_root)
        ftp_download(ftp["server"], ftp["username"], ftp["password"], data_path, ftp["source"], limit)


'''
This module make using of DropBox easier. It reads the api key from EgorovSystem.

This module denpends on the `dropbox` entry of [EgorovSystem](https://github.com/FFTYYY/EgorovSystem).
### Egorov System Data Format
    "{api_key}"
'''

from egorovsystem import Egorov, get_variable
from typing import Literal, Any
from .dropbox import Dropbox
import warnings

_dropbox_initialized = False
_dropbox = None

def get_dropbox_instance():
    global _dropbox
    global _dropbox_initialized
    
    if not _dropbox_initialized:
        try: 
            api_key = get_variable("dropbox").strip()
            _dropbox = Dropbox(api_key)
        except Exception:
            _dropbox = None
    
    return _dropbox

def setdropbox(data: Any, tar_path: str, format: Literal["binary" , "str" , "pickle"] = "pickle"):
    '''This function denpends on the `dropbox` entry of [EgorovSystem](https://github.com/FFTYYY/EgorovSystem).
    ### Egorov System Data Format
        `{api_key}`
    '''

    dropbox = get_dropbox_instance()
    if dropbox is None:
        warnings.warn("no aws account found. upload fail.")
        return False
    
    return dropbox.set(data, tar_path, format)

def getdropbox(tar_path: str, format: Literal["binary" , "str" , "pickle"] = "pickle") -> Any:
    '''This function denpends on the `dropbox` entry of [EgorovSystem](https://github.com/FFTYYY/EgorovSystem).
    ### Egorov System Data Format
        `{api_key}`
    '''

    dropbox = get_dropbox_instance()
    if dropbox is None:
        warnings.warn("no aws account found. get fail.")
        return None
    
    return dropbox.get(tar_path, format)

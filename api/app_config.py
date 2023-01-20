from functools import cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    sudo_path : str = '/usr/bin/sudo'
    app_name: str = "Counter API"
    admin_email: str = "counter@seznam.cz"
    items_per_user: int = 50

    description  = """
Python API for various work 🚀
## counter
You will be able to:
* **set number for any string** (_not implemented_).
* **get number for any string** (_DONE - implemented_).
"""

@cache
def get_settings():
    return Settings()
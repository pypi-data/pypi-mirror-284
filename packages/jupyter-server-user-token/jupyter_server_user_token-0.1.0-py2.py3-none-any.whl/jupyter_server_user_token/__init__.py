import os
import jupyter_server

__version__ = "0.1.0"

def _load_jupyter_server_extension(serverapp: jupyter_server.serverapp.ServerApp):
    """
    This function is called when the extension is loaded and is responsible for
    adding the user token to the environment (JUPYTER_SERVER_USER_TOKEN).
    """
    os.environ["JUPYTER_SERVER_USER_TOKEN"] = serverapp.identity_provider.token

def _jupyter_server_extension_points():
    """
    Returns a list of dictionaries with metadata describing
    where to find the `_load_jupyter_server_extension` function.
    """
    return [{"module": "jupyter_server_user_token"}]
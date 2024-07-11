SETTINGS = {"api_key": "", "region": None, "api_key_in_header": True}

HEADERS = {}


def connect(api_key, region=None, api_key_in_header=True):
    """setup the connection for all following API calls

    Keyword arguments:
    api_key -- string
    region  -- region object (optional)
    """

    SETTINGS["api_key"] = api_key
    SETTINGS["region"] = region
    SETTINGS["api_key_in_header"] = api_key_in_header

    if api_key_in_header:
        HEADERS["X-Riot-Token"] = SETTINGS["api_key"]


def get_headers():
    return HEADERS


def get_base_url(region):
    if region is not None:
        SETTINGS["region"] = region

    if SETTINGS["region"] is None:
        raise Exception("region is required.")

    return SETTINGS["region"]["proxy"]["url"]


def get_main_params():
    if not SETTINGS["api_key_in_header"]:
        return {"api_key": SETTINGS["api_key"]}
    return {}

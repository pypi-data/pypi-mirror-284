from riot import APIRequest

VERSION = "v1"


def account_by_puuid(puuid, region=None):
    url = "/riot/account/{VERSION}/accounts/by-puuid/{puuid}"
    api = APIRequest(url.format(version=VERSION, puuid=puuid))
    return api.get(region), api.data


def account_by_game_name_tagline(game_name, tag_line, region=None):
    api = APIRequest(f"/riot/account/{VERSION}/accounts/{game_name}/{tag_line}")
    return api.get(region), api.data

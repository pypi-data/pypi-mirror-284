from riot import APIRequest

VERSION = "v5"


def active_game_by_summoner_id(summoner_id, region=None):
    api = APIRequest(
        f"/lol/spectator/{VERSION}/active-games/by-summoner/{summoner_id}"
    )
    return api.get(region), api.data

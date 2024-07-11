from riot import APIRequest

VERSION = "v1"


def entries_by_summoner_id(summoner_id, region=None):
    api = APIRequest(f"/tft/league/{VERSION}/entries/by-summoner/{summoner_id}")
    return api.get(region), api.data

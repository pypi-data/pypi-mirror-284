from riot import APIRequest

VERSION = "v4"


def entries_by_summoner(summoner_puuid, region=None):
    api = APIRequest(
        f"/lol/league/{VERSION}/entries/by-summoner/{summoner_puuid}"
    )
    return api.get(region), api.data

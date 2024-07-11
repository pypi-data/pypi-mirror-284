from riot import APIRequest

VERSION = "v4"


def summoner_by_encrypted_account_id(encrypted_account_id, region=None):
    api = APIRequest(
        f"/lol/summoner/{VERSION}/summoners/by-account/{encrypted_account_id}"
    )
    return api.get(region), api.data


def summoner_by_encrypted_PUUID(encrypted_PUUID, region=None):
    api = APIRequest(
        f"/lol/summoner/{VERSION}/summoners/by-puuid/{encrypted_PUUID}"
    )
    return api.get(region), api.data


def summoner_by_encrypted_summoner_id(encrypted_summoner_id, region=None):
    api = APIRequest(
        f"/lol/summoner/{VERSION}/summoners/{encrypted_summoner_id}"
    )
    return api.get(region), api.data

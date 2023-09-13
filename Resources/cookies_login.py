# TODO:
#  Generate cookies for avoiding cookies modal

c = [
    {
        "domain": ".instagram.com",
        "expirationDate": 1710141854.14143,
        "hostOnly": 'false',
        "httpOnly": 'false',
        "name": "csrftoken",
        "path": "/",
        "sameSite": "unspecified",
        "secure": 'true',
        "session": 'false',
        "storeId": "0",
        "value": "avzxauT0FlpDpG2oeHHOVpeMLxoZhXzC",
        "id": '1'
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1710141818,
        "hostOnly": 'false',
        "httpOnly": 'true',
        "name": "ig_did",
        "path": "/",
        "sameSite": "unspecified",
        "secure": 'true',
        "session": 'false',
        "storeId": "0",
        "value": "07EFC442-DC6B-4526-9D75-B5D1B1A34318",
        "id": 2
    },
    {
        "domain": ".instagram.com",
        "expirationDate": '1710141854.141487',
        "hostOnly": 'false',
        "httpOnly": 'false',
        "name": "mid",
        "path": "/",
        "sameSite": "unspecified",
        "secure": 'true',
        "session": 'false',
        "storeId": "0",
        "value": "ZQFjngAEAAHtSP72JNnKbuuvcys6",
        "id": '3'
    }
]


def cookie(c):
    for _ in c:
        return _


cookie(c)

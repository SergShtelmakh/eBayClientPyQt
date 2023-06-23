import datetime

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

from config import sandbox

def searchItems(text):
    try:
        api = Connection(domain=sandbox["domain"], appid=sandbox["app_id"], config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': text})

        assert(response.reply.ack == 'Success')
        assert(type(response.reply.timestamp) == datetime.datetime)
        assert(type(response.reply.searchResult.item) == list)
        return response.reply.searchResult

    except ConnectionError as e:
        print(e)
        return []


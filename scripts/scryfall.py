import requests



def search(data):
    url = 'https://api.scryfall.com'
    search = '/cards/search'
    query = '?q="Akroma"&unique=art'
    data = requests.get(url+search+'?q="'+data+'"&unique=art')
    return data

def getcard(data):
    url = 'https://api.scryfall.com'
    search = '/cards'
    query = data
    data = requests.get(url+search+'/'+data)
    data = data.json()
    #print(data)
    #data = data['data']
    return data

import sqlite3



def insert_card(owner,card):
    conn = sqlite3.connect('collection_db.db')
    c = conn.cursor()
    cardlist = []
    print(card)
    for x in card:
        print(x)
    query = '''insert into mtg_collection values ("%s","%s","%s","%s","%s","%s","%s","%s","%s")''' % (owner,card['id'],card['name'],card['mana_cost'],card['type_line'],card['oracle_text'],card['image_uris']['normal'],card['image_uris']['small'],1)
    print(query)
    c = c.execute(query)
    conn.commit()
    conn.close()

def query_db(query):
    conn = sqlite3.connect('collection_db.db')
    c = conn.cursor()
    c = c.execute(query)
    response = []
    for row in c:
        response.append(row)
    conn.commit()
    conn.close()
    return response


def create_collection_table():
    conn = sqlite3.connect('collection_db.db')
    c = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS mtg_collection
        (owner blob,
        id blob,
        name blob,
        mana_cost blob,
        type_line blob,
        oracle_text blob,
        image_normal blob,
        image_small blob,
        qty integer)
        '''
    c.execute(query)
    conn.commit()
    conn.close()

def create_owners_table():
    conn = sqlite3.connect('collection_db.db')
    c = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS owners
        (ownername blob UNIQUE)
        '''
    c.execute(query)
    conn.commit()
    conn.close()

def create_decks_table():
    conn = sqlite3.connect('collection_db.db')
    c = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS decks
        (deckname blob,
        owner blob)
        '''
    c.execute(query)
    conn.commit()
    conn.close()

def get_decks():
    conn = sqlite3.connect('collection_db.db')
    c = conn.cursor()
    query = '''select * from decks
        '''
    c.execute(query)
    response = []
    for row in c:
        response.append(row)
    conn.commit()
    conn.close()
    return response

def get_owners():
    conn = sqlite3.connect('collection_db.db')
    c = conn.cursor()
    query = '''select * from owners order by lower(ownername) asc
        '''
    c.execute(query)
    response = []
    for row in c:
        response.append(row)
    conn.commit()
    conn.close()
    return response

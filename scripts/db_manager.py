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


def create_db():
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

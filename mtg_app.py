from scripts import scryfall, db_manager
from flask import Flask, render_template, request,redirect, url_for



whoami = 'Paul'

app = Flask(__name__)
app.debug=True


@app.route('/mycards')
def mycards():
    query = 'select * from mtg_collection where owner = "%s"' % whoami
    data = db_manager.query_db(query)
    return render_template('mycards.html',data=data)

@app.route('/add/<id>')
def addcard(id):
    data = scryfall.getcard(id)
    db_manager.insert_card(whoami,data)
    return redirect(url_for('mycards'))

@app.route('/change/<id>/<qty>')
def removecard(id,qty):
    if int(qty) < 1:
        query = 'delete from mtg_collection where owner = "%s" and id = "%s"' % (whoami,id)
    else:
        query = 'update mtg_collection set qty = %s where owner = "%s" and id = "%s"' % (qty,whoami,id)

    db_manager.query_db(query)
    return redirect(url_for('mycards'))


@app.route('/', methods=['GET','POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        print(request)
        data = request.form.get('searchid')
        print('DATA',data)
        data = scryfall.search(data)
        data = data.json()
        data=data['data']
        for x in data[0]:
            print(x)

        return render_template('home.html', data=data)

    else:

        return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

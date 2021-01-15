from scripts import scryfall, db_manager
from flask import Flask, render_template, request,redirect, url_for



whoami = 'Paul'

app = Flask(__name__)
app.debug=True


@app.route('/mycards<user>')
def mycards(user):
    query = 'select * from mtg_collection where owner = "%s"' % user
    data = db_manager.query_db(query)
    return render_template('mycards.html',data=data,user=user)

@app.route('/add/<id>', methods=['GET','POST'])
def addcard(id):
    user = request.form.get('user')
    print('user selected',user
    )

    data = scryfall.getcard(id)
    db_manager.insert_card(user,data)
    return redirect(url_for('mycards', user=user))

@app.route('/change/<user>/<id>/<qty>')
def removecard(user,id,qty):
    if int(qty) < 1:
        query = 'delete from mtg_collection where owner = "%s" and id = "%s"' % (user,id)
    else:
        query = 'update mtg_collection set qty = %s where owner = "%s" and id = "%s"' % (qty,user,id)

    db_manager.query_db(query)
    return redirect(url_for('mycards',user=user))


@app.route('/manageowners', methods=['GET','POST'])
def manageowners():
    print(request.method)
    if request.method == 'POST':
        data = request.form.get('ownername')
        print('DATA',data)

        db_manager.query_db('insert into owners values("%s")' % (data))
        owners = db_manager.get_owners()

        return render_template('owners.html', data=owners)

    else:
        owners = db_manager.get_owners()
        print(owners)

        return render_template('owners.html', data=owners)


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

        owners = db_manager.get_owners()

        return render_template('home.html', data=data, owners=owners)

    else:

        return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

import requests
from flask import Flask, render_template, request,redirect, url_for

url = 'https://api.scryfall.com'
search = '/cards/search'
query = '?q="Akroma"'



app = Flask(__name__)
app.debug=True


@app.route('/', methods=['GET','POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        print(request)
        data = request.form.get('searchid')
        print('DATA',data)
        data = requests.get(url+search+'?q="'+data+'"')
        data = data.json()
        data=data['data']
        for x in data[0]:
            print(x)

        return render_template('home.html', data=data)

    else:

        return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

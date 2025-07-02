from flask import Flask, render_template,request, redirect, url_for
from pgAdmin0 import *
from datetime import datetime
now = datetime.now()
app = Flask(__name__)


res=seve()
orders = order() 
@app.route('/')
def index():
    return render_template('pgrigis.html',)

@app.route('/item', methods=['GET', 'POST'])
def item():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        isbuy = flascpr(username, password)
        if isbuy == True:
            return render_template('item.html', item=res, username=username, isbuy=isbuy)
        else:
            return render_template('pgrigis.html', error='Вы не купили подписку')
        

@app.route('/add_to_order', methods=['POST'])
def add_to_order():
    id = request.form['id'] 
    username = request.form['name']
    price = request.form['price']
    order_date = now.date()
    print(id, username, price, order_date)
    add_order(id,username, price, order_date)
    return redirect(url_for('index'))

@app.route('/orders')
def orders():
    orders = order()
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
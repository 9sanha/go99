from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

import requests
app = Flask(__name__)



client = MongoClient('localhost', 27017)

db = client.dbsparta


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index_4.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['give_name']
    address_receive = request.form['give_address']
    number_receive = request.form['give_number']
    quantity_receive = request.form['give_quantity']
    doc = {
        'name':name_receive,
        'address':address_receive,
        'number':number_receive,
        'quantity':quantity_receive
    }
    db.remind.insert_one(doc)
    return jsonify({'msg': '주문이 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    order_list = list(db.remind.find({}, {'_id': False}))
    return jsonify({'orderList': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

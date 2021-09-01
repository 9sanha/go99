from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient
app = Flask(__name__)



client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta

@app.route('/')
def main():
    return render_template('login2.html')

# 주문하기(POST) API
@app.route('/login', methods=['POST'])
def login():
    name_receive = request.form['name_give']
    img_url = request.form['img_url_give']
    print(img_url,name_receive)
    doc = {
        'name': name_receive,
        'quantity': img_url,
        }
    db.userinfo.insert_one(doc)
    return jsonify({'msg': '저장이 완료되었습니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

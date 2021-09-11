from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index_5.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_stars():
    StarList = list(db.mystar.find({}, {'_id': False}).sort('like',-1))
    return jsonify({'StarList':StarList})


@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']
    target = db.mystar.find_one({'name': name_receive})
    cur_like = target['like']
    new_like = cur_like+1

    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})
    return jsonify({'msg': '좋아요'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']
    db.mystar.delete_one({'name': name_receive})
    return jsonify({'msg': '삭제요'})

@app.route('/api/unlike', methods=['POST'])
def unlike_star():
    name_receive = request.form['name_give']
    target = db.mystar.find_one({'name': name_receive})
    cur_like = target['like']
    if cur_like==0:
        return jsonify({'msg': '더 내릴 수 없어요'})
    else:
        new_like = cur_like-1
        db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})
        return jsonify({'msg': '내려요'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta




@app.route('/')
def main():  # put application's code here
    return render_template('main.html')



@app.route('/genre', methods=['GET'])
def view_movie():
    givegenre = request.args.get('givegenre')
    movie_list = list(db.movie_info.find({'genre':givegenre}, {'_id': False}))
    return jsonify({'movieList': movie_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

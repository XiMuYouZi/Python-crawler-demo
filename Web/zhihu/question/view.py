from . import question
from flask import jsonify, request
import json
import pymongo
from bson import BSON, json_util

dept_data = [
    {
        'name': '部门1',
        'id': 12345
    },
    {
        'name': '部门2',
        'id': 12346
    }
]

MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'
client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]
collection = 'question'


# get方法
@question.route('/<int:page>', methods=['GET', ])
def get_question(page):
    datas = db[collection].find({}, {'_id': 0}).skip(20 * page).limit(20)
    users = []
    for data in datas:
        user = json.dumps(data, default=json_util.default)
        user = json.loads(user)
        users.append(user)
    return json.dumps(users)

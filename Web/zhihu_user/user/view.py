from . import user
from flask import jsonify, request
import json
import pymongo
from bson import BSON, json_util

user_data = [
    {
        'id': 1,
        'name': '张三',
        'age': 23
    },
    {
        'id': 2,
        'name': '李四',
        'age': 24
    }
]

MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]
collection = 'users'


@user.route('/<int:id>', methods=['GET', ])
def get(id):
    for user in user_data:
        if user['id'] == id:
            return jsonify(status='success', user=user)


# 实现MongoDB的翻页查询
@user.route('/users', methods=['GET', 'POST'])
def users():
    print(request.headers, request.data, request.form)
    page = request.form.get("page", type=int, default=None)
    datas = db[collection].find({}, {'name': 1, 'description': 1, 'headline': 1, '_id': 0}).skip(20 * page).limit(20)
    users = []
    for data in datas:
        user = json.dumps(data, default=json_util.default)
        user = json.loads(user)
        users.append(user)
    return json.dumps(users)

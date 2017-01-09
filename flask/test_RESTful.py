#!/usr/bin/env python
# coding=utf-8
'''
构造RESTful接口示例
使用flask 完成get ,post ,update, delete的功能

get:

JSON格式的数据，是经过Flask框架的 jsonify模块格式化过的数据
通过参数，检索tasks数组。如果参数传过来的id不存在于数组内，我们需要返回错误代码404，按照HTTP的规定，404意味着是"Resource Not Found"，资源未找到。

如果找到任务在内存数组内，我们通过jsonify模块将字典打包成JSON格式，并发送响应到客户端上。就像处理一个实体字典一样

post:

 request.json里面包含请求数据，如果不是JSON或者里面没有包括title字段，将会返回400的错误代码。

当创建一个新的任务字典，使用最后一个任务id数值加1作为新的任务id（最简单的方法产生一个唯一字段）。这里允许不带description字段，默认将done字段值为False。

http://www.cnblogs.com/vovlie/p/4178077.html
'''

from flask import Flask,jsonify,abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1/tasks/<int:task_id>',methods=['GET'])
def get_tasks(task_id):
    task = filter(lambda t:t['id']==task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'tasks':tasks[0]}) 

from flask import make_response,request
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'NOT FOUND'}),404)



@app.route('/todo/api/v1/tasks/',methods=['POST'])
def create_task():
    if not request.json or not request.json:
        abort(400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201



@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=False)

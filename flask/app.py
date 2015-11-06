#!/usr/bin/env python
# coding=utf-8
from flask import Flask 
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1> this document crries a cookie</h1>')
    response.set_cookie('answer','42')
    return response

if __name__ == "__main__":
    app.run(debug=True)

    #Cookie:answer=42
    #Host:127.0.0.1:5000
    #make_response 函数可以接受多个参数和视图函数的返回值一样，然后在对应对像上调用各种方法进一步设置响应。
    #上面例子就是创建了一个响应，然后设置了cookie.

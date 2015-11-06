from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('what is your name?', validators = [Required()])
    submit = SubmitField('submit')
#Required 添加验证，如果不为空则验证通过.






@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods = ['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html',name=name, form=form)
#验证是NameForm类实例用于表示表单，没有输入时为none,提交表单后数据 能够所有验证波函数接受，validate_on_submit方法返回true
#用户第一次访问程序时,服务器会收到一个没有表单数据的 GET 请求,所以 validate_on_ submit() 将返回 False。if 语句的内容将被跳过,通过渲染模板处理请求
#服务器收到一个包含数据的 POST 请求。validate_on_submit() 会调用 name 字段上附属的 Required() 验证函数,数据 #不为空则通过验证，用户输入的名字可通过字段的 data 属性获取。在 if 语句中, 把名字赋值给局部变量 name

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()

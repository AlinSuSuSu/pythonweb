from flask import Flask
from flask import request#请求
from flask import make_response#响应
from flask import render_template#模板
from flask_bootstrap import Bootstrap
from flask_moment import Moment#本地化日期和时间
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


app = Flask(__name__)#Flask类的构造函数只有一个必须制定的参数，即程序主模块或包的名字
app.config['SECRET_KEY'] = 'HARD TO GUESS STRING'#设置Flask-WTF
bootstrap = Bootstrap(app) #初始化Flask-Bootstrap
moment = Moment(app)#初始化Flask-moment
#设置路由：处理URL和函数之间关系的函数成为路由
@app.route('/')
def index():
    '''user_agent= request.headers.get('User-Agent')
    response = make_response('this is a cookie')
    response.set_cookie('answer','42')
    #return response'''
    return render_template('index.html')


@app.route('/user/<name1>')
def user(name1):
    return render_template('user.html',name = name1)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

#启动服务器
if __name__ == '__main__':
    app.run(debug=True,port = 7775)#设置端口号为7775
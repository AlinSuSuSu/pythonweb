from flask import Flask
from flask import request#请求
from flask import make_response#响应
from flask import render_template#模板
from flask_bootstrap import Bootstrap
from flask_moment import Moment#本地化日期和时间
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
#重定向和用户会话
from flask import session, redirect, url_for
#flash消息
from flask import flash
from datetime import datetime
app = Flask(__name__)
#Flask类的构造函数只有一个必须制定的参数，即程序主模块或包的名字
app.config['SECRET_KEY'] = 'HARD TO GUESS STRING'#设置Flask-WTF
bootstrap = Bootstrap(app) #初始化Flask-Bootstrap
moment = Moment(app)#初始化Flask-moment


#表单
class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[Required()])
    submit = SubmitField('Submit')

#设置路由：处理URL和函数之间关系的函数成为路由
@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))#用于重定向
    return render_template('index.html',form=form, name=session.get('name'), current_time=datetime.utcnow())


@app.route('/user/<name1>')
def user(name1):
    return render_template('user.html',name = name1)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

#启动服务器
if __name__ == '__main__':
    app.run(debug=True,port = 7775)#设置端口号为7775

from flask_bootstrap import Bootstrap #引用bootstrap扩展
from flask import Flask,render_template#引用模板
from flask_moment import Moment#本地化日期和时间
from datetime import datetime
#表单类
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
#重定向和用户会话
from flask import session, redirect, url_for
#flash消息
from flask import flash

import os
basedir = os.path.abspath(os.path.dirname(__file__))
#表单
class NameForm(FlaskForm):
    name = StringField("What's your name?",validators=[Required()])
    submit = SubmitField('Submit')

app = Flask(__name__)

#配置通用密钥
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/',methods=['GET','POST'])
def index():

    form = NameForm()
    if form.validate_on_submit():
         old_name = session.get('name')
         if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
         session['name'] = form.name.data
         return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'), known = session.get['known',False],current_time=datetime.utcnow())



@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name1=name)

#自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



if __name__ == '__main__':
    app.run(debug=True,port=7775)
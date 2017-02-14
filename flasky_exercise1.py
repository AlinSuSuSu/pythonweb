'''from flask import Flask, render_template

app = Flask(__name__)
#app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>hello,index</h1>"


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
'''
from flask.ext.bootstrap import Bootstrap #引用bootstrap矿建
from flask import Flask,render_template#引用模板
from flask.ext.moment import Moment#本地化日期和时间
from datetime import datetime
#表单类
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
#重定向和用户会话
from flask import session, redirect, url_for
#flash消息
from flask import flash
#配置数据库
from flask.ext.sqlalchemy import  SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#表单
class NameForm(Form):
    name = StringField("What's your name?",validators=[Required()])
    submit = SubmitField('Submit')





app = Flask(__name__)

#配置通用密钥
app.config['SECRET_KEY'] = 'hard to guess string'
#配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

#将数据库表定义为模型
'''
class Role(db.Model):

    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
'''



bootstrap = Bootstrap(app)
moment = Moment(app)
#创建表
'''db.create_all()
# 插入行
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='user')
user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)
# 准备把对象写入数据库之前，先将其添加到会话中
#db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
# 再用commit方法提交会话
#db.session.commit()
#new
'''
@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
         '''old_name = session.get('name')
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user=User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        '''
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
    app.run(debug=True)
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:AIOUseven132456@103.40.24.222:3306/flask_demo?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Games(db.Model):
    #定义表名
    __tablename__ = 'games'
    #定义字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    appid = db.Column(db.String(200))
    date = db.Column(db.String(200))
    de = db.Column(db.String(200))
    push = db.Column(db.String(200))
    price = db.Column(db.String(200))
    pinlun = db.Column(db.Integer)
    createtime =db.Column(db.DateTime)


@app.route('/')
def hello_world():
    gamelist = Games.query.all()
    print(gamelist)
    return render_template('test.html',gamelist=gamelist)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='8080')
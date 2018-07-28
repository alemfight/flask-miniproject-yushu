from flask import Flask
from app.models.book import db
#flask对象创建
def create_app():
    app = Flask(__name__)
    # 用这种方法要求配置文件参数必须全部大写
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app

#注册蓝图
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
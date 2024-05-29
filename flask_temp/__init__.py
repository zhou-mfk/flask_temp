# 如果导入了未使用则配置在此处
__all__ = ["TempDb"]

from flask import Flask, render_template

from config import config
from flask_temp.ext import db, migrate
from flask_temp.models import TempDb


def create_app(config_name: str | None):
    # 创建 Flask 程序实例
    app = Flask(__name__)

    # 使用对象的方式引入配置文件
    if config_name is None:
        config_name = "dev"
    app.config.from_object(config[config_name])

    # 增加心跳地址
    @app.route("/check_health")
    def check_health():
        return "Status: OK"

    register_logging(app)
    # 引入扩展
    register_extensions(app)
    # 注册蓝图
    register_blueprints(app)
    register_commands(app)
    register_errors(app)

    return app


def register_logging(app: Flask) -> None:
    pass


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app: Flask) -> None:
    pass


def register_commands(app: Flask) -> None:
    # 添加命令
    pass


def register_errors(app: Flask) -> None:
    @app.errorhandler(400)
    def bad_request(e):
        return render_template("errors/400.html"), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("errors/500.html"), 500

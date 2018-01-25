from Web.zhihu_user.dept import dept
from Web.zhihu_user.user import user
from Web.zhihu_user.error import error
from flask import Flask
from Web.zhihu_user.main import main

app = Flask(__name__)

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(dept, url_prefix='/dept')
app.register_blueprint(error, url_prefix='/error')
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(main, url_prefix='/index')

if __name__ == '__main__':
    app.run()

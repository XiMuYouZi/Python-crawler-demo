from Web.zhihu.question import question
from Web.zhihu.user import user
from Web.zhihu.error import error
from flask import Flask
from Web.zhihu.main import main
from flask.ext.script import Manager

app = Flask(__name__)

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(question, url_prefix='/question')
app.register_blueprint(error, url_prefix='/error')
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(main, url_prefix='/index')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()

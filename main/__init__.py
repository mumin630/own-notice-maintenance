from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('main.config')

db = SQLAlchemy(app)

import main.views.index_view  # noqa
import main.views.test_view  # noqa
import main.views.notice_view  # noqa

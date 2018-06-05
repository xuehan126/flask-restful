from flask import Flask
from api import init_api
import settings

app = Flask(__name__)
app.config.from_object(settings.Config)
init_api(app)


if __name__ == '__main__':
    app.run()
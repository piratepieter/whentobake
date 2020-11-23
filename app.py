from flask import Flask

myapp = Flask(__name__)


@myapp.route('/')
def app():
    return "My beautiful app"


if __name__ == "__main__":
    myapp.run()
import wol
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello! This is a Wake On Lan Server, powered by Flask :D'


@app.route('/wake')
def wake():
    wol.wake_on_lan()
    return 'Send WOL packet!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')

import wol
from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/wake',methods=['post'])
def wake():
    wol.wake_on_lan()
    return 'WOL packet sent.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8004')

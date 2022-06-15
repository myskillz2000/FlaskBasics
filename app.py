from flask import Flask
app = Flask(__name__)

app.config.from_pyfile('settings.py')

@app.route('/')
@app.route('/home')
def index():
    return "Whatever you want here."

if __name__ == '__main__':
    app.run()

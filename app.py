from flask import Flask, render_template
app = Flask(__name__)

app.config.from_pyfile('settings.py')

@app.route('/')
@app.route('/home')
def index():
    return render_template('basic.html')

if __name__ == '__main__':
    app.run()

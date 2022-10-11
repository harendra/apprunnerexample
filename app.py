from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('blank.html')


@app.route('/test_api')
def test_api():
    return "This is the result from the test API"



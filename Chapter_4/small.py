from flask import Flask, redirect, request, jsonify

app = Flask('basic app')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('http://www.google.com/search?q=%s' % request.args['q'])
    else:
        return jsonify({"result": "OK"})
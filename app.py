# imports 
from flask import Flask, request, render_template, jsonify
import pickle

# init
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello_world():
    """
        GET /
    """
    return render_template("main.html")


@app.route('/prediction', methods=['POST'])
def prediction():
    """
        POST /prediction
    """
    inputs = [(x) for x in request.form.values()]
    prediction = model.predict([inputs[0]])[0]
    result = "Safe" if prediction == 1 else "Dangerous"
    return render_template('main.html', res=result, website=inputs[0])

@app.route('/checkurl', methods=['GET'])
def check_url():
    """
        GET /checkurl?url=...
    """
    query_url = request.args.get('url')
    prediction = model.predict([query_url])[0]
    res = "good" if prediction == 1 else "bad"
    return jsonify({'url': query_url, "result" : res})

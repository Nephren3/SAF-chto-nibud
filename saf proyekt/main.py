from flask import Flask, render_template, jsonify
import json

app=Flask(__name__)


@app.route("/")
def index():
    with open('data.json', 'r', encoding='utf-8') as f:
        alldata = json.load(f)
    return render_template('index.html', regions=alldata['regions'])

if __name__ == '__main__':
    app.run(debug=True)





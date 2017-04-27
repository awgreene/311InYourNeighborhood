from flask import Flask, render_template, request, jsonify
import os,sys
import json
sys.path.append(os.getcwd()+"/src")

app = Flask(__name__)

port = int(os.getenv('PORT', 7080))

@app.route('/')
def home():
    return render_template('index.html')

from constants import DataConstants
from pull import PullFunctions
@app.route('/api/pull', methods=['POST'])
def populate_ngrams():
    return jsonify(PullFunctions.pull_from_url(DataConstants.data_url))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

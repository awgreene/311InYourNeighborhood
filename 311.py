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
from ensemble import RF_Pred
from train import ColTraining
@app.route('/api/pull', methods=['POST'])
def pull_results():
    table_json,acc = RF_Pred.get_col_pred("CASE_TITLE")
    return jsonify({"Accuracy":acc,"TableData":table_json})


@app.route('/api/train', methods=['POST'])
def train_col_based():
    ColTraining.train_col_based()
    return ("Training Complete")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

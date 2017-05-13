from flask import Flask, render_template, request, jsonify
import os,sys
import json
sys.path.append(os.getcwd()+"/src")

app = Flask(__name__)

port = int(os.getenv('PORT', 7080))

@app.route('/')
def home():
    return render_template('flaskIndex.html')

from constants import DataConstants
from ensemble import RF_Pred
from train import ColTraining
@app.route('/api/pull', methods=['POST'])
def pull_results():
    mvp=request.json['prefixText'].replace('Training Complete. Most important column is ','')
    table_json,acc = RF_Pred.get_col_pred(mvp)
    return json.dumps({"Accuracy":acc,"TableData":table_json,"MVP":mvp})

@app.route('/static/api/pull', methods=['POST'])
def static_pull_results():
    mvp=request.json['prefixText'].replace('Training Complete. Most important column is ','')
    table_json,acc = RF_Pred.get_col_pred(mvp)
    return json.dumps({"Accuracy":acc,"TableData":table_json,"MVP":mvp})

@app.route('/api/train', methods=['POST'])
def train_col_based():
    most_valuable_col=ColTraining.train_col_based()
    return ("Training Complete. Most important column is "+most_valuable_col)

@app.route('/static/api/train', methods=['POST'])
def static_train_col_based():
    most_valuable_col=ColTraining.train_col_based()
    return ("Training Complete. Most important column is "+most_valuable_col)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

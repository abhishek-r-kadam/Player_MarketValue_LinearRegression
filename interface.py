from flask import Flask,request,jsonify
from project_app.utils import MarketValuePredict

app = Flask(__name__)

@app.route("/")
def home_api():
    return "Predict Players Market value"

@app.route("/predict")
def predict():
    
    data = request.form
    
    club = data["club"]
    position = data["position"]
    page_views = data["page_views"]
    fpl_value = data["fpl_value"]
    fpl_sel = data["fpl_sel"]
    fpl_points = data["fpl_points"]
    region = data["region"]
    new_foreign = data["new_foreign"]
    age_cat = data["age_cat"]
    big_club = data["big_club"]
    new_signing = data["new_signing"]
    
    
    model = MarketValuePredict(club,position,page_views,fpl_value,fpl_sel,fpl_points,region,new_foreign,age_cat,big_club,new_signing)
    
    prediction_result = model.predict_mv()
    
    return jsonify({"Predicted Market value":prediction_result})

app.run(debug = True)
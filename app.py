from flask import Flask, render_template, request
from models.tabular.tabpfn_predictor import predict_tabpfn

app = Flask(__name__)

@app.route("/")
def home():
    # return "Hello Yashitaa!! Flask is working!"
    return render_template("index.html")

@app.route("/tabular")
def tabular():
    return render_template("tabular.html")

@app.route("/imaging")
def imaging():
    return render_template("imaging.html")

@app.route("/predict-tabular", methods=["POST"])
def predict_tabular_route():

    input_data = {
        "male": int(request.form["male"]),
        "age": int(request.form["age"]),
        "education": int(request.form.get("education", 1)),
        "currentSmoker": int(request.form["currentSmoker"]),
        "cigsPerDay": float(request.form.get("cigsPerDay", 0)),
        "BPMeds": int(request.form["BPMeds"]),
        "prevalentStroke": int(request.form["prevalentStroke"]),
        "prevalentHyp": int(request.form["prevalentHyp"]),
        "diabetes": int(request.form["diabetes"]),
        "totChol": float(request.form["totChol"]),
        "sysBP": float(request.form["sysBP"]),
        "diaBP": float(request.form["diaBP"]),
        "BMI": float(request.form["BMI"]),
        "heartRate": float(request.form["heartRate"]),
        "glucose": float(request.form["glucose"])
    }

    prediction, confidence = predict_tabpfn(input_data)

    return render_template(
        "result_tabular.html",
        **input_data,
        prediction=prediction,
        confidence=confidence
    )


if __name__ =="__main__":
    app.run(debug=True)

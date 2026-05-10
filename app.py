from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

# Import your working Tabular predictor AND your new MRI segmenter
from models.tabular.tabpfn_predictor import predict_tabpfn
from models.mri.acdc_segmenter import segment_mri_unet

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    # return "Hello Yashitaa!! Flask is working!"
    return render_template("index.html")

@app.route("/tabular")
def tabular():
    return render_template("tabular.html")

@app.route("/mri")
def mri():
    return render_template("mri.html")

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

@app.route("/predict-mri", methods=["POST"])
def predict_mri():
    # Safely catch the file regardless of input name in HTML
    uploaded_file = request.files.get("mri_image") or request.files.get("mri_scan")

    if not uploaded_file or uploaded_file.filename == "":
        return redirect(url_for("mri"))

    # Save original scan
    filename = secure_filename(uploaded_file.filename)
    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    uploaded_file.save(upload_path)

    # Run your OpenCV U-Net processing script
    segmented_filename, metrics = segment_mri_unet(upload_path, UPLOAD_FOLDER)

    # Render the side-by-side dashboard
    return render_template(
        "result_mri.html",
        original_image=filename,
        segmented_image=segmented_filename,
        metrics=metrics
    )

if __name__ =="__main__":
    app.run(debug=True)

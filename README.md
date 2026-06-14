# IntelliCardiac: Multi-Stage Cardiovascular Disease Detection Web Portal

## Overview
This project is a comprehensive clinical diagnostic web portal designed to assess cardiovascular disease (CVD) risk through two distinct, state-of-the-art machine learning paradigms. Built with a Flask backend and a responsive, dark-mode clinical dashboard frontend, the platform bridges the gap between complex deep learning architectures and actionable medical telemetry.

The portal consists of two primary modules:
1. **Behavioral Risk Analysis (Tabular Data):** Evaluates outpatient 10-year CVD risk using patient vitals.
2. **Cardiac MRI Diagnostics Suite (Radiomics Workflow):** An end-to-end spatial imaging pipeline for structural heart disease classification.

---

## Key Features

### Module 1: Behavioral Risk Analysis (TabPFN)
* **Dataset:** Framingham Heart Study (balanced to 1,000 instances).
* **Inputs:** 15 distinct clinical parameters (demographics, behavioral history, physiological vitals).
* **Preprocessing:** Automated median-based imputation for missing records.
* **Model:** TabPFN (Tabular Prior-Data Fitted Network) for ultra-fast, in-context learning.
* **Output:** "High Risk" vs "Low Risk" classification alongside a dynamic Algorithmic Confidence Score.

### Module 2: End-to-End Radiomics Workflow (MRI)
* **Dataset:** ACDC (Automated Cardiac Diagnosis Challenge).
* **Stage 1 (Segmentation):** A 2D U-Net isolates the Myocardium (MYO) and Left Ventricle (LV) cavity, generating a live mask overlay on the uploaded short-axis cine-MRI tensor.
* **Stage 2 (Feature Extraction):** Dynamically extracts 35 volumetric, morphological, and textural features (e.g., Ejection Fraction, Myocardial Mass, Sphericity Index).
* **Stage 3 (Classification):** An XGBoost multi-class inference engine evaluates the 35 features to output a probability distribution across 5 pathological states:
  - **NOR:** Normal Cardiac Structure
  - **MINF:** Myocardial Infarction
  - **DCM:** Dilated Cardiomyopathy
  - **HCM:** Hypertrophic Cardiomyopathy
  - **ARV:** Abnormal Right Ventricle

---

## Technology Stack
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Asynchronous DOM manipulation, dynamic telemetry bars).
* **Backend:** Python, Flask, Werkzeug (Secure File Handling).
* **Machine Learning & Vision:** * `TabPFN` (Foundation Model for Tabular Data)
  * `XGBoost` (Tree-based Multi-class Inference)
  * `OpenCV` & `Pillow (PIL)` (Tensor parsing and mask blending)
  * `NumPy` & `Pandas` (Data standardization and feature extraction)

---

## Project Structure
```text
cvd_project/
│
├── app.py                            # Main Flask server and route handling
├── requirements.txt                  # Project dependencies
│
├── models/
│   ├── tabular/
│   │   └── tabpfn_predictor.py       # Preprocessing and TabPFN inference script
│   └── mri/
│       └── acdc_segmenter.py         # 3-Stage U-Net & XGBoost radiomics pipeline
│
├── static/
│   ├── css/                          # Stylesheets for the dark-mode dashboard
│   ├── js/                           # Interactive scripts for live telemetry
│   └── uploads/                      # Secure directory for temporal MRI processing
│
└── templates/
    ├── base.html                     # Main HTML wrapper
    ├── index.html                    # Portal landing page
    ├── tabular.html                  # Behavioral Risk input form
    ├── result_tabular.html           # TabPFN output flashcard
    ├── mri.html                      # MRI Drag & Drop workstation
    └── result_mri.html               # 3-Stage Radiomics clinical dashboard
```

---

## Installation & Setup
1. Clone the repository:
```text
git clone [https://github.com/YourUsername/IntelliCardiac-Web-Portal.git](https://github.com/YourUsername/IntelliCardiac-Web-Portal.git)
cd IntelliCardiac-Web-Portal
```
2. Create a virtual environment (Recommended):
```text
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies:
```text
pip install -r requirements.txt
```
(Ensure opencv-python, pillow, flask, numpy, pandas, xgboost, and tabpfn are included in your requirements).

4. Run the application:
```text
python app.py
```
5. Access the Portal:
Open your web browser and navigate to: http://127.0.0.1:5000

---

## Usage Guide
For General Screening: Navigate to the Behavioral Risk tab. Enter the patient's vitals (Age, Systolic BP, Cholesterol, etc.) and click Submit to view the TabPFN-generated 10-year risk assessment.

For Advanced Imaging: Navigate to the MRI Diagnostics tab. Upload a short-axis cardiac MRI slice (.png, .jpeg, or .dcm). The system will execute the U-Net segmentation, calculate 35 radiomic features, and display the XGBoost 5-class pathology probability dashboard.

---

## Contributors
* Shivam Sharma (22BCS104)
* Yashita Arya (22BCS120)
* Lipi Rani (22BCS125)

Guided by: 
Dr. Ram Prakash Sharma <br>
Asstt. Professor, Department of Computer Science & Engineering<br>
National Institute of Technology, Hamirpur 

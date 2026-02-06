import pandas as pd
from tabpfn import TabPFNClassifier

# Globals (loaded once)
_model = None
_feature_columns = None


def _load_model():
    global _model, _feature_columns

    if _model is not None:
        return

    # Load dataset
    data = pd.read_csv("data/framingham_tabpfn_ready.csv")
    data_small = data.sample(n=1000, random_state=42)

    X = data_small.drop("TenYearCHD", axis=1)
    y = data_small["TenYearCHD"]

    # X = data.drop("TenYearCHD", axis=1)
    # y = data["TenYearCHD"]

    _feature_columns = X.columns.tolist()

    _model = TabPFNClassifier(
    device="cpu",
    ignore_pretraining_limits=True
    )

    _model.fit(X, y)


def predict_tabpfn(input_dict):
    _load_model()

    # Convert input to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensure correct column order
    input_df = input_df[_feature_columns]

    pred = _model.predict(input_df)[0]
    prob = _model.predict_proba(input_df)[0][1]

    label = "High Risk" if pred == 1 else "Low Risk"
    confidence = int(prob * 100)

    return label, confidence

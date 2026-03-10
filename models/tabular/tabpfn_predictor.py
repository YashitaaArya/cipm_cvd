import pandas as pd
from tabpfn import TabPFNClassifier

# Globals (loaded once)
_model = None
_feature_columns = None

def _load_model():
    global _model, _feature_columns

    if _model is not None:
        return

    # 1. Load the original dataset
    data = pd.read_csv("framingham_heart_study.csv")
    
    # 2. Fix missing values (Fill blanks with the median of that column)
    data.fillna(data.median(), inplace=True)

    # 3. Separate the dataset into Low Risk (0) and High Risk (1)
    chd_0 = data[data["TenYearCHD"] == 0]
    chd_1 = data[data["TenYearCHD"] == 1]

    # 4. BALANCE THE DATA: Take exactly 500 of each
    # (Since there are only ~640 high-risk patients total, 500 is perfect)
    chd_0_sampled = chd_0.sample(n=500, random_state=42)
    chd_1_sampled = chd_1.sample(n=500, random_state=42)
    
    # 5. Combine them back together and shuffle them
    data_balanced = pd.concat([chd_0_sampled, chd_1_sampled])
    data_balanced = data_balanced.sample(frac=1, random_state=42) # Shuffle

    # 6. Split features and target
    X = data_balanced.drop("TenYearCHD", axis=1)
    y = data_balanced["TenYearCHD"]

    _feature_columns = X.columns.tolist()

    # 7. Train the TabPFN Foundation Model
    _model = TabPFNClassifier(
        device="cpu",
        ignore_pretraining_limits=True
    )

    _model.fit(X, y)

# def _load_model():
#     global _model, _feature_columns

#     if _model is not None:
#         return

#     # Load dataset
#     data = pd.read_csv("data/framingham_heart_study.csv")
#     data_small = data.sample(n=1000, random_state=42)

#     X = data_small.drop("TenYearCHD", axis=1)
#     y = data_small["TenYearCHD"]

#     # X = data.drop("TenYearCHD", axis=1)
#     # y = data["TenYearCHD"]

#     _feature_columns = X.columns.tolist()

#     _model = TabPFNClassifier(
#     device="cpu",
#     ignore_pretraining_limits=True
#     )

#     _model.fit(X, y)


def predict_tabpfn(input_dict):
    _load_model()

    # Convert input to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensure correct column order
    input_df = input_df[_feature_columns]

    pred = _model.predict(input_df)[0]
    prob = _model.predict_proba(input_df)[0][1]

    label = "High Risk" if pred == 1 else "Low Risk"
    confidence = int(abs((prob-0.5)*2)*100)

    return label, confidence

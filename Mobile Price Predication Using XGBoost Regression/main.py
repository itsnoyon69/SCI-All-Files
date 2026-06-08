# =========================================
# IMPORT LIBRARIES
# =========================================

import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

from xgboost import XGBRegressor

# =========================================
# LOAD DATASET
# =========================================

df = pd.read_csv(
    "data/device_specs_structured_dataset.csv"
)

# =========================================
# REMOVE NULL VALUES
# =========================================

df.dropna(inplace=True)

# =========================================
# SELECT IMPORTANT FEATURES
# =========================================

selected_features = [

    "brand",
    "ram_raw",
    "storage_raw",
    "battery_raw",
    "chipset",
    "rear_camera_raw",
    "fast_charging_raw",
    "display_type",
    "network_support",
    "nfc_raw",
    "list_price_inr"

]

df = df[selected_features]

# =========================================
# CLEAN RAM
# =========================================

df["ram_raw"] = df["ram_raw"].astype(str)

df["ram_raw"] = df["ram_raw"].str.extract(r'(\d+)')

df["ram_raw"] = df["ram_raw"].astype(float)

# =========================================
# CLEAN STORAGE
# =========================================

df["storage_raw"] = df["storage_raw"].astype(str)

df["storage_raw"] = df["storage_raw"].str.extract(r'(\d+)')

df["storage_raw"] = df["storage_raw"].astype(float)

# =========================================
# CLEAN BATTERY
# =========================================

df["battery_raw"] = df["battery_raw"].astype(str)

df["battery_raw"] = df["battery_raw"].str.extract(r'(\d+)')

df["battery_raw"] = df["battery_raw"].astype(float)

# =========================================
# CLEAN CAMERA
# =========================================

df["rear_camera_raw"] = df["rear_camera_raw"].astype(str)

df["rear_camera_raw"] = df["rear_camera_raw"].str.extract(r'(\d+)')

df["rear_camera_raw"] = df["rear_camera_raw"].astype(float)

# =========================================
# CLEAN FAST CHARGING
# =========================================

df["fast_charging_raw"] = df["fast_charging_raw"].astype(str)

df["fast_charging_raw"] = df["fast_charging_raw"].str.extract(r'(\d+)')

df["fast_charging_raw"] = df["fast_charging_raw"].astype(float)

# =========================================
# NFC YES/NO
# =========================================

df["nfc_raw"] = df["nfc_raw"].map({

    "Yes": 1,
    "No": 0

})

# =========================================
# 5G SUPPORT
# =========================================

df["network_support"] = df["network_support"].astype(str)

df["network_support"] = df["network_support"].apply(

    lambda x: 1 if "5G" in x else 0

)

# =========================================
# REMOVE NULL AGAIN
# =========================================

df.dropna(inplace=True)

# =========================================
# LABEL ENCODING
# =========================================

brand_encoder = LabelEncoder()

chipset_encoder = LabelEncoder()

display_encoder = LabelEncoder()

df["brand"] = brand_encoder.fit_transform(
    df["brand"]
)

df["chipset"] = chipset_encoder.fit_transform(
    df["chipset"]
)

df["display_type"] = display_encoder.fit_transform(
    df["display_type"]
)

# =========================================
# FEATURES & TARGET
# =========================================

X = df.drop("list_price_inr", axis=1)

y = df["list_price_inr"]

# =========================================
# TRAIN TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)

# =========================================
# XGBOOST MODEL
# =========================================

model = XGBRegressor(

    n_estimators=300,
    learning_rate=0.05,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42

)

# =========================================
# TRAIN MODEL
# =========================================

model.fit(X_train, y_train)

# =========================================
# PREDICTION
# =========================================

y_pred = model.predict(X_test)

# =========================================
# EVALUATION
# =========================================

mae = mean_absolute_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print()

print("MAE :", mae)

print("R2 Score :", r2)

# =========================================
# SAVE MODEL
# =========================================

joblib.dump(

    model,
    "models/mobile_price_model.pkl"

)

joblib.dump(

    brand_encoder,
    "models/brand_encoder.pkl"

)

joblib.dump(

    chipset_encoder,
    "models/chipset_encoder.pkl"

)

joblib.dump(

    display_encoder,
    "models/display_encoder.pkl"

)

print()

print("Model Saved Successfully")
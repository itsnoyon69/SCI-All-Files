# =========================================
# IMPORT LIBRARIES
# =========================================

import streamlit as st
import numpy as np
import joblib
import os

# =========================================
# BASE DIRECTORY
# =========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

# =========================================
# LOAD MODEL & ENCODERS
# =========================================

model = joblib.load(

    os.path.join(
        BASE_DIR,
        "models",
        "mobile_price_model.pkl"
    )

)

brand_encoder = joblib.load(

    os.path.join(
        BASE_DIR,
        "models",
        "brand_encoder.pkl"
    )

)

chipset_encoder = joblib.load(

    os.path.join(
        BASE_DIR,
        "models",
        "chipset_encoder.pkl"
    )

)

display_encoder = joblib.load(

    os.path.join(
        BASE_DIR,
        "models",
        "display_encoder.pkl"
    )

)

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(

    page_title="AI Smartphone Price Predictor",
    page_icon="📱",
    layout="centered"

)

# =========================================
# TITLE
# =========================================

st.title("📱 AI Smartphone Price Predictor")

st.markdown(

    "Build your dream smartphone and predict its estimated market price."

)

# =========================================
# BRAND OPTIONS
# =========================================

all_brands = sorted([

    brand.title()

    for brand in brand_encoder.classes_

])

brand_options = [

    "Select Brand"

] + all_brands

# =========================================
# BRAND SECTION
# =========================================

st.header("🏷 Brand")

brand = st.selectbox(

    "Select Your Smartphone Brand",

    brand_options,

    index=0

)

# =========================================
# OS LOGIC
# =========================================

os_type = "Unknown"

if brand != "Select Brand":

    if brand.lower() == "apple":

        os_type = "iOS"

    else:

        os_type = "Android"

# =========================================
# SHOW OS
# =========================================

st.header("💻 Operating System")

st.info(

    f"Selected Operating System: {os_type}"

)

# =========================================
# PROCESSOR FAMILY
# =========================================

processor_family_options = [

    "Select Processor Family"

]

if os_type == "iOS":

    processor_family_options += [

        "Apple Bionic"

    ]

elif os_type == "Android":

    processor_family_options += [

        "Snapdragon",
        "MediaTek",
        "Exynos",
        "Tensor",
        "Kirin",
        "Unisoc"

    ]

processor_family = st.selectbox(

    "Select Processor Family",

    processor_family_options,

    index=0

)

# =========================================
# PROCESSOR OPTIONS
# =========================================

processor_options = [

    "Select Processor"

]

# SNAPDRAGON

if processor_family == "Snapdragon":

    processor_options += [

        "Snapdragon 4 Gen 2",
        "Snapdragon 6 Gen 1",
        "Snapdragon 7 Gen 1",
        "Snapdragon 7+ Gen 2",
        "Snapdragon 7 Gen 3",
        "Snapdragon 8 Gen 1",
        "Snapdragon 8+ Gen 1",
        "Snapdragon 8 Gen 2",
        "Snapdragon 8 Gen 3",
        "Snapdragon 8 Elite"

    ]

# MEDIATEK

elif processor_family == "MediaTek":

    processor_options += [

        "Helio G85",
        "Helio G99",
        "Dimensity 6100+",
        "Dimensity 7200",
        "Dimensity 8200",
        "Dimensity 8300",
        "Dimensity 9200",
        "Dimensity 9300",
        "Dimensity 9400"

    ]

# EXYNOS

elif processor_family == "Exynos":

    processor_options += [

        "Exynos 1280",
        "Exynos 1380",
        "Exynos 1480",
        "Exynos 2200",
        "Exynos 2400"

    ]

# GOOGLE TENSOR

elif processor_family == "Tensor":

    processor_options += [

        "Tensor G2",
        "Tensor G3",
        "Tensor G4"

    ]

# APPLE

elif processor_family == "Apple Bionic":

    processor_options += [

        "A14 Bionic",
        "A15 Bionic",
        "A16 Bionic",
        "A17 Pro",
        "A18",
        "A18 Pro"

    ]

# KIRIN

elif processor_family == "Kirin":

    processor_options += [

        "Kirin 9000S",
        "Kirin 9010"

    ]

# UNISOC

elif processor_family == "Unisoc":

    processor_options += [

        "Unisoc T606",
        "Unisoc T760"

    ]

# =========================================
# PROCESSOR SELECT
# =========================================

processor = st.selectbox(

    "Select Processor",

    processor_options,

    index=0

)

# =========================================
# PERFORMANCE
# =========================================

st.header("⚡ Performance")

ram = st.selectbox(

    "Select RAM",

    [

        "Select RAM",

        "4 GB",
        "6 GB",
        "8 GB",
        "12 GB",
        "16 GB",
        "24 GB"

    ],

    index=0

)

storage = st.selectbox(

    "Select Storage",

    [

        "Select Storage",

        "64 GB",
        "128 GB",
        "256 GB",
        "512 GB",
        "1 TB"

    ],

    index=0

)

ufs = st.selectbox(

    "Select UFS Version",

    [

        "Select UFS",

        "UFS 2.2",
        "UFS 3.1",
        "UFS 4.0"

    ],

    index=0

)

memory_slot = st.selectbox(

    "Memory Card Slot",

    [

        "Select Option",

        "Yes",
        "No"

    ],

    index=0

)

# =========================================
# DISPLAY
# =========================================

st.header("🖥 Display")

display_type = st.selectbox(

    "Display Type",

    [

        "Select Display",

        "IPS LCD",
        "OLED",
        "AMOLED",
        "Super AMOLED",
        "Dynamic AMOLED",
        "LTPO AMOLED"

    ],

    index=0

)

refresh_rate = st.selectbox(

    "Refresh Rate",

    [

        "Select Refresh Rate",

        "60Hz",
        "90Hz",
        "120Hz",
        "144Hz",
        "165Hz"

    ],

    index=0

)

screen_size = st.number_input(

    "Screen Size (Inches)",

    5.0,
    8.0,
    6.7

)

resolution = st.selectbox(

    "Screen Resolution",

    [

        "Select Resolution",

        "HD+",
        "FHD+",
        "1.5K",
        "2K"

    ],

    index=0

)

# =========================================
# CAMERA
# =========================================

st.header("📷 Camera")

main_camera = st.number_input(

    "Main Camera MP",

    8,
    200,
    50

)

ultrawide_camera = st.number_input(

    "Ultrawide Camera MP",

    0,
    100,
    12

)

telephoto_camera = st.number_input(

    "Telephoto Camera MP",

    0,
    100,
    10

)

front_camera = st.number_input(

    "Front Camera MP",

    5,
    100,
    32

)

ois = st.selectbox(

    "OIS Support",

    [

        "Select Option",

        "Yes",
        "No"

    ],

    index=0

)

# =========================================
# BATTERY
# =========================================

st.header("🔋 Battery")

battery = st.number_input(

    "Battery Capacity (mAh)",

    3000,
    8000,
    5000

)

fast_charging = st.number_input(

    "Fast Charging Watt",

    10,
    240,
    67

)

wireless = st.selectbox(

    "Wireless Charging",

    [

        "Select Option",

        "Yes",
        "No"

    ],

    index=0

)

# =========================================
# NETWORK & FEATURES
# =========================================

st.header("📡 Network & Features")

support_5g = st.selectbox(

    "5G Support",

    [

        "Select Option",

        "Yes",
        "No"

    ],

    index=0

)

wifi = st.selectbox(

    "WiFi Support",

    [

        "Select Option",

        "WiFi 5",
        "WiFi 6",
        "WiFi 6E",
        "WiFi 7"

    ],

    index=0

)

bluetooth = st.selectbox(

    "Bluetooth Version",

    [

        "Select Bluetooth",

        "5.0",
        "5.1",
        "5.2",
        "5.3",
        "5.4"

    ],

    index=0

)

nfc = st.selectbox(

    "NFC Support",

    [

        "Select Option",

        "Yes",
        "No"

    ],

    index=0

)

fingerprint = st.selectbox(

    "Fingerprint Sensor",

    [

        "Select Option",

        "Yes",
        "No"

    ],

    index=0

)

sim_type = st.selectbox(

    "SIM Type",

    [

        "Select SIM Type",

        "Single SIM",
        "Dual SIM",
        "Dual SIM + eSIM"

    ],

    index=0

)

ip_rating = st.selectbox(

    "IP Rating",

    [

        "Select IP Rating",

        "No Rating",
        "IP52",
        "IP54",
        "IP67",
        "IP68"

    ],

    index=0

)

# =========================================
# PREDICT BUTTON
# =========================================

if st.button("💰 Predict Smartphone Price"):

    # =====================================
    # ENCODING
    # =====================================

    try:

        brand_encoded = brand_encoder.transform(

            [brand.lower()]

        )[0]

    except:

        brand_encoded = 0

    try:

        processor_encoded = chipset_encoder.transform(

            [processor]

        )[0]

    except:

        processor_encoded = 0

    try:

        display_encoded = display_encoder.transform(

            [display_type]

        )[0]

    except:

        display_encoded = 0

    # =====================================
    # CONVERT VALUES
    # =====================================

    ram_value = 0

    if ram != "Select RAM":

        ram_value = int(
            ram.split()[0]
        )

    storage_value = 0

    if storage != "Select Storage":

        if storage == "1 TB":

            storage_value = 1024

        else:

            storage_value = int(
                storage.split()[0]
            )

    refresh_value = 0

    if refresh_rate != "Select Refresh Rate":

        refresh_value = int(
            refresh_rate.replace("Hz", "")
        )

    support_5g_value = 1 if support_5g == "Yes" else 0

    nfc_value = 1 if nfc == "Yes" else 0

    memory_slot_value = 1 if memory_slot == "Yes" else 0

    fingerprint_value = 1 if fingerprint == "Yes" else 0

    wireless_value = 1 if wireless == "Yes" else 0

    ois_value = 1 if ois == "Yes" else 0

    # =====================================
    # INPUT ARRAY
    # =====================================

    input_data = np.array([

        [

            brand_encoded,
            ram_value,
            storage_value,
            battery,
            processor_encoded,
            main_camera,
            fast_charging,
            display_encoded,
            support_5g_value,
            nfc_value

        ]

    ])

    # =====================================
    # PREDICTION
    # =====================================

    prediction = model.predict(

        input_data

    )

    # =====================================
    # OUTPUT
    # =====================================

    st.success(

        f"📱 Estimated Smartphone Price: ₹ {prediction[0]:,.0f}"

    )
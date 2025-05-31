# FintechPySparkETL 🚀  
> End-to-end PySpark pipeline for fintech transaction analysis, fraud detection using machine learning, and interactive dashboarding via Streamlit.

## 📌 Overview

**FintechPySparkETL** is a modular, scalable, and production-oriented data pipeline built using Apache Spark. The project performs the following:

- 🧼 **ETL**: Ingests raw transaction data and cleanses, transforms, and enriches it.
- 🤖 **Machine Learning**: Flags potentially fraudulent transactions using a trained classification model.
- 📊 **Dashboard**: A Streamlit-based UI for visualizing and reviewing suspicious activity.

This pipeline is designed with performance, transparency, and extensibility in mind, ideal for real-world fintech data operations.

---

## 🗂️ Project Structure
FintechPySparkETL/
│
├── data/ # Input and output datasets
│ └── sample_transactions.csv
│
├── etl/ # PySpark ETL job scripts
│ └── fraud_etl_pipeline.py
│
├── ml/ # ML pipeline and model training
│ └── generate_ml_data.py
│ └── fraud_model.py
│
├── dashboard/ # Streamlit dashboard
│ └── app.py
│
├── _archive/ # Archived local dev files (excluded from repo)
├── .gitignore
├── requirements.txt
├── README.md
└── run_etl.sh # Shell script to run ETL job


---

## ⚙️ Technologies Used

- **Apache Spark (PySpark)** — distributed data processing
- **Scikit-learn** — ML model training (Random Forest)
- **Streamlit** — interactive dashboard
- **Pandas / NumPy / Faker** — data manipulation and generation
- **Git** — version control

---

## 🔍 Features

- ✅ Batch ETL processing using Spark
- ✅ Feature engineering for fraud detection
- ✅ Trained ML model with fraud flagging
- ✅ Real-time data exploration via Streamlit
- ✅ Clean structure and scalable architecture

---

## 🚀 Getting Started

### 1. Install Prerequisites

- [Install Spark 3.5.1](https://spark.apache.org/downloads.html)
- Python 3.9+
- Java 11+
- Git

### 2. Clone the Repository

```bash
git clone https://github.com/Redtgrlily/FintechPySparkETL.git
cd FintechPySparkETL

### 3. Set Up Environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt

### 4. Generate Sample Data
python ml/generate_ml_data.py

### 5. Run the ETL Job
spark-submit etl/fraud_etl_pipeline.py

### 6. Launch the Dashboard
cd dashboard
streamlit run app.py

### Sample Output
data/processed_transactions.csv: includes features + fraud prediction column

Streamlit dashboard allows filtering, exploring, and visualizing fraud patterns.

### .gitignore Highlights
This project excludes:

Spark binaries

Large data files

Environment folders

Local IDE/project settings

See .gitignore for details.

### Contributing
Contributions are welcome! Fork the repo, make your changes, and open a pull request.

###  License
MIT License. See LICENSE file for details.

### Author
Kaitlyn McCormick
github.com/Redtgrlily
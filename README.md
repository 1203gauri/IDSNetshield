# 🛡️ NetShield: AI-Powered Intrusion Detection System

NetShield is a deep learning-based Intrusion Detection System (IDS) designed to analyze and classify network traffic in real time using LSTM models. It is built with the CSE-CIC-IDS2018 dataset and aims to detect a wide range of cyber threats, including DoS, DDoS, SQL Injection, Bot attacks, and more.

---

## 🔗 Demo

Check out the live demo here: [NetShield Live Demo](https://www.loom.com/share/94686d795d364988b3da85c79e3976c0?sid=aab3f246-f9e6-4525-8f40-a800b2cc733c)  

## 🚀 Features

- 🧠 **LSTM-based Intrusion Detection Model**
- 📊 **Real-Time Detection of Cyber Attacks**
- ⚡ **Preprocessing and Normalization of Network Traffic**
- 🧪 **Evaluation with Accuracy, Precision, Recall, and F1-score**
- 💾 Model saving and loading for future use
- 🔐 Designed to integrate into scalable security solutions

---

## 📁 Dataset

Used multiple CSV files from the [CSE-CIC-IDS2018 dataset](https://www.unb.ca/cic/datasets/ids-2018.html), including:
- DDOS attack-LOIC-UDP
- DoS attacks-Slowloris
- DoS attacks-GoldenEye
- FTP-BruteForce
- Bot
- SQL Injection

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Pandas, NumPy, Scikit-learn
- Flask (for deployment)
- Google Colab (for development)

---

## 🧬 Model Architecture

- **LSTM (128 units)** + Dropout(0.3)
- **LSTM (64 units)** + Dense(32 ReLU) + Dropout(0.2)
- Output Layer with **Sigmoid Activation**

---

## 🔄 Preprocessing Steps

1. Combine multiple CSV files into one dataset.
2. Drop irrelevant features (e.g., IPs, Timestamps).
3. Label transformation (Benign = 0, Attack = 1).
4. Fill missing values.
5. Feature normalization using `StandardScaler`.
6. Train-test split and reshape data for LSTM.

---

## 🧪 Evaluation Metrics

- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**

---

## 💻 How to Run

```bash
# Clone the repo
git clone https://github.com/1203gauri/netshield-ids.git
cd netshield-ids

# (Optional) Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run training
python train_model.py

# Run evaluation
python evaluate_model.py

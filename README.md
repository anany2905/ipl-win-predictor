# 🏏 IPL Win Predictor

An advanced **Machine Learning + NLP-based web application** that predicts the winning probability of an IPL match in real-time.

This project combines **data science, cricket analytics, and sentiment analysis** to simulate match momentum and provide an interactive experience similar to platforms like Dream11 and Cricbuzz.

---

## 🚀 Live Features

• 📊 Real-Time Win Probability Prediction  
• 📈 Dynamic Match Momentum Graph  
• 🏆 Winning Team Prediction  
• 🎯 Turning Point Detection  
• 🧠 NLP-Based Live Commentary & Sentiment Score  
• 🎨 Dream11-Inspired Modern UI  
• ⚡ Fast & Interactive Web App (Streamlit)

---

## 🧠 Machine Learning + NLP Workflow

### 🔹 Machine Learning Pipeline
1. Data Collection from IPL datasets  
2. Data Cleaning & Preprocessing  
3. Feature Engineering:
   - Runs Left  
   - Balls Remaining  
   - Wickets Left  
   - Current Run Rate (CRR)  
   - Required Run Rate (RRR)  
4. Model Training using Random Forest Classifier  
5. Model Evaluation & Accuracy Testing  
6. Model Saving (Joblib)

---

### 🔹 NLP Integration

To enhance prediction realism, **Natural Language Processing (NLP)** is used:

• 🎙️ Generates match commentary based on game situation  
• 📊 Converts commentary → sentiment score using TextBlob  
• 🧠 Adds sentiment as feature representing **match momentum & pressure**

#### Sentiment Meaning:
- +1 → Batting team dominating  
- 0 → Balanced match  
- -1 → Bowling team dominating  

👉 This makes the system a **Hybrid ML + NLP Model**

---

## 📊 Dataset

The project uses IPL datasets from Kaggle:

• `matches.csv` → Match-level data  
• `deliveries.csv` → Ball-by-ball data  

---

## 🛠️ Tech Stack

• **Programming Language:** Python  
• **Libraries:**
  - Pandas  
  - NumPy  
  - Scikit-learn  
  - Matplotlib  
  - TextBlob  
• **Framework:** Streamlit  
• **Deployment:** Streamlit Cloud  

---

## 📂 Project Structure
ipl-win-predictor/
│
├── app.py # Streamlit Web App
├── model.pkl # Trained ML Model
├── columns.pkl # Feature Columns
├── matches.csv # Dataset
├── deliveries.csv # Dataset
├── requirements.txt # Dependencies
├── README.md # Documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/your-username/ipl-win-predictor.git
cd ipl-win-predictor


### 2️⃣ Install dependencies
pip install -r requirements.txt


### 3️⃣ Run the app
streamlit run app.py


---

## 📊 Model Performance

• Accuracy: ~99%  
• Handles real-time match situations  
• Captures both statistical and psychological aspects  

---

## 🔮 Future Improvements

• 🏏 Integration with live match APIs  
• 📱 Mobile responsive UI  
• 🎨 Team logos & animations  
• 📊 Advanced analytics dashboard  
• 🤖 AI chatbot for match insights  

---

## 👨‍💻 Author

**Anany Kanjolia**  
B.Tech ECE  
Aspiring Software Engineer | Data Scientist | ML Engineer  

---

## ⭐ Support

If you like this project:

⭐ Give it a star on GitHub  
📢 Share it with others  
💡 Feel free to contribute  

---

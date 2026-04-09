🏏 IPL Win Predictor

An advanced Machine Learning-based web application that predicts the winning probability of an IPL match in real-time. This project combines data science, cricket analytics, and modern UI design to deliver an interactive experience similar to platforms like Dream11 and Cricbuzz.

⸻

🚀 Live Features
	•	📊 Real-Time Win Probability Prediction
	•	📈 Dynamic Match Momentum Graph
	•	🏆 Winning Team Prediction
	•	🎯 Turning Point Detection in Match
	•	🎨 Dream11-Inspired Modern UI
	•	⚡ Fast & Interactive Web App (Streamlit)

⸻

🧠 Machine Learning Workflow
	1.	Data Collection from IPL datasets
	2.	Data Cleaning & Preprocessing
	3.	Feature Engineering:
	•	Runs Left
	•	Balls Remaining
	•	Wickets Left
	•	Current Run Rate (CRR)
	•	Required Run Rate (RRR)
	4.	Model Training using Random Forest Classifier
	5.	Model Evaluation & Accuracy Testing
	6.	Deployment using Streamlit

⸻

📊 Dataset

The project uses IPL datasets:
	•	matches.csv → Match-level data
	•	deliveries.csv → Ball-by-ball data

⸻

🛠️ Tech Stack
	•	Programming Language: Python
	•	Libraries:
	•	Pandas
	•	NumPy
	•	Scikit-learn
	•	Matplotlib
	•	Framework: Streamlit
	•	Deployment: Streamlit Cloud


📂 Project Structure

ipl-win-predictor/
│
├── app.py              # Main Streamlit app
├── model.pkl           # Trained ML model
├── columns.pkl         # Feature columns
├── matches.csv         # Dataset
├── deliveries.csv      # Dataset
├── requirements.txt    # Dependencies
├── README.md           # Project documentation

⚙️ Installation & Setup

1️⃣ Clone the repository
git clone https://github.com/your-username/ipl-win-predictor.git
cd ipl-win-predictor

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py


🌐 Deployment

This project is deployed using Streamlit Cloud.
You can access the live app here:


🧠 Future Improvements
	•	🏏 Integration with live match data
	•	📱 Mobile responsive UI
	•	🎨 Team logos & animations
	•	📊 Advanced analytics dashboard

⸻

👨‍💻 Author

Anany Kanjolia
B.Tech ECE | Aspiring Software & Data Science & Machine Learning Engineer

⸻

⭐ If you like this project

Give it a ⭐ on GitHub and share it!
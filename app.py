import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="IPL Predictor", layout="wide")

# 🔥 BACKGROUND (NO FILE NEEDED)
def set_bg():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
                    url("https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .block-container {
        background: rgba(0, 0, 0, 0.65);
        padding: 20px;
        border-radius: 15px;
    }

    h1, h2, h3, label {
        color: white;
    }

    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

set_bg()

# Load model
model = joblib.load('model.pkl')
columns = joblib.load('columns.pkl')

st.title("🏏 IPL Elite Win Predictor")

teams = [
    'Mumbai Indians','Chennai Super Kings','Royal Challengers Bangalore',
    'Kolkata Knight Riders','Delhi Capitals','Rajasthan Royals',
    'Sunrisers Hyderabad','Punjab Kings','Gujarat Titans','Lucknow Super Giants'
]

cities = ['Mumbai','Delhi','Chennai','Kolkata','Hyderabad','Bangalore','Jaipur','Ahmedabad']

# Inputs
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Batting Team", teams)
    target = st.number_input("Target", min_value=1)

    overs_completed = st.number_input("Overs Completed", min_value=0, max_value=20, step=1)
    balls_completed = st.selectbox("Balls in Over (0-5)", [0,1,2,3,4,5])

with col2:
    bowling_team = st.selectbox("Bowling Team", teams)
    score = st.number_input("Current Score", min_value=0)
    wickets = st.slider("Wickets Left", 0, 10)

city = st.selectbox("City", cities)

# 🔥 Calculations
total_balls = overs_completed * 6 + balls_completed
balls_remaining = 120 - total_balls
overs = overs_completed + balls_completed / 6

runs_left = target - score
run_rate = score / overs if overs > 0 else 0
rrr = (runs_left * 6) / balls_remaining if balls_remaining > 0 else 0

# 🏏 Match Summary
st.markdown(f"""
### 🏏 Match Summary
- **Score:** {score}/{10-wickets}  
- **Overs:** {overs_completed}.{balls_completed}  
- **Target:** {target}  
- **Runs Left:** {runs_left}  
- **CRR:** {round(run_rate,2)} | **RRR:** {round(rrr,2)}
""")

# Prediction
if st.button("🚀 Predict Winner"):

    input_df = pd.DataFrame({
        'runs_left':[runs_left],
        'balls_remaining':[balls_remaining],
        'wickets_left':[wickets],
        'target':[target],
        'run_rate':[run_rate],
        'rrr':[rrr]
    })

    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df['batting_team_' + batting_team] = 1
    input_df['bowling_team_' + bowling_team] = 1
    input_df['city_' + city] = 1

    input_df = input_df[columns]

    result = model.predict_proba(input_df)[0]

    batting_prob = result[1]*100
    bowling_prob = result[0]*100

    # 🏆 Winner
    if batting_prob > bowling_prob:
        st.success(f"🏆 {batting_team} Winning ({round(batting_prob,2)}%)")
    else:
        st.success(f"🏆 {bowling_team} Winning ({round(bowling_prob,2)}%)")

    st.info(f"{batting_team}: {round(batting_prob,2)}%  |  {bowling_team}: {round(bowling_prob,2)}%")

    # 📊 GRAPH
    st.subheader("📊 Match Momentum")

    overs_list = np.linspace(1, overs if overs > 1 else 1.5, 15)
    prob_list = []

    for o in overs_list:
        balls_rem = int(120 - (o * 6))
        rr = score / o if o > 0 else 0
        rrr_temp = (runs_left * 6) / balls_rem if balls_rem > 0 else 0

        temp_df = pd.DataFrame({
            'runs_left':[runs_left],
            'balls_remaining':[balls_rem],
            'wickets_left':[wickets],
            'target':[target],
            'run_rate':[rr],
            'rrr':[rrr_temp]
        })

        for col in columns:
            if col not in temp_df.columns:
                temp_df[col] = 0

        temp_df['batting_team_' + batting_team] = 1
        temp_df['bowling_team_' + bowling_team] = 1
        temp_df['city_' + city] = 1

        temp_df = temp_df[columns]

        prob = model.predict_proba(temp_df)[0][1]
        prob_list.append(prob*100)

    # 🎯 Turning Point
    turning_point = np.argmax(prob_list)

    # 🎨 Graph
    col_center = st.columns([1,2,1])

    with col_center[1]:
        fig, ax = plt.subplots(figsize=(6,4))

        ax.plot(overs_list, prob_list, linewidth=2)

        prob_array = np.array(prob_list)

        # Zones
        ax.fill_between(overs_list, prob_array, where=(prob_array > 50), alpha=0.3)
        ax.fill_between(overs_list, prob_array, where=(prob_array <= 50), alpha=0.1)

        # 🔥 Smart Label
        x = overs_list[turning_point]
        y = prob_list[turning_point]

        offset = 15 if y < 50 else -20

        ax.scatter(x, y, s=80)
        ax.annotate("Turning Point",
                    (x, y),
                    textcoords="offset points",
                    xytext=(0, offset),
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3"))

        ax.set_xlabel("Overs")
        ax.set_ylabel(f"{batting_team} Win %")
        ax.set_title("Win Probability Curve")
        ax.set_ylim(0, 100)

        st.pyplot(fig)
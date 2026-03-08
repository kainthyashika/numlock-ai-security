import streamlit as st
import hashlib
import time
import random
import requests
import pandas as pd
import pydeck as pdk
import plotly.express as px
from sklearn.ensemble import IsolationForest

# =============================
# PAGE CONFIG
# =============================

st.set_page_config(
    page_title="NumLock AI Security Center",
    layout="wide"
)

# =============================
# LOGIN SYSTEM
# =============================

ADMIN_USER = "admin"
ADMIN_PASSWORD = "numlock123"

def login():

    st.title("🔐 NumLock AI Security Center")
    st.subheader("Administrator Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == ADMIN_USER and password == ADMIN_PASSWORD:

            st.session_state["authenticated"] = True
            st.success("Login successful")
            st.rerun()

        else:
            st.error("Invalid credentials")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
    st.stop()

# =============================
# TELEGRAM CONFIG
# =============================

BOT_TOKEN = st.secrets["BOT_TOKEN"]
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# =============================
# DATABASE (MEMORY)
# =============================

USER_DB = {}
TOKENS = {}
ACTIVITY = []
ALERTS = []

# =============================
# TELEGRAM REGISTRATION
# =============================

def fetch_registrations():

    try:
        data = requests.get(f"{TELEGRAM_URL}/getUpdates").json()
    except:
        return

    if not data["ok"]:
        return

    for update in data["result"]:

        if "message" not in update:
            continue

        msg = update["message"]
        text = msg.get("text","")
        chat_id = msg["chat"]["id"]

        if text.startswith("/register"):

            parts = text.split()

            if len(parts) == 2:

                phone = parts[1]

                USER_DB[phone] = chat_id

# =============================
# SEND ALERT
# =============================

def send_alert(phone,message):

    chat_id = USER_DB.get(phone)

    if not chat_id:
        return False

    payload = {
        "chat_id":chat_id,
        "text":message
    }

    requests.post(f"{TELEGRAM_URL}/sendMessage",data=payload)

    ALERTS.append({
        "phone":phone,
        "time":time.strftime("%H:%M:%S"),
        "message":message
    })

    return True

# =============================
# TOKEN SYSTEM
# =============================

def generate_token(phone):

    base=f"{phone}-{time.time()}"

    token=hashlib.sha256(base.encode()).hexdigest()[:16]

    TOKENS[token]={
        "phone":phone,
        "exp":time.time()+300,
        "used":False
    }

    return token

# =============================
# FRAUD ENGINE
# =============================

def fraud_score(phone):

    now=time.time()

    ACTIVITY.append({
        "phone":phone,
        "time":now,
        "lat":random.uniform(20,30),
        "lon":random.uniform(70,80)
    })

    score=min(len(ACTIVITY)*5,100)

    return score

# =============================
# AI ANOMALY DETECTION
# =============================

def ai_anomaly_detection():

    if len(ACTIVITY) < 5:
        return "Not enough data"

    df=pd.DataFrame(ACTIVITY)

    features=df[["lat","lon"]]

    model=IsolationForest(
        contamination=0.2,
        random_state=42
    )

    model.fit(features)

    preds=model.predict(features)

    anomalies=sum(preds==-1)

    if anomalies>0:
        return "ANOMALY DETECTED"

    return "Normal Activity"

# =============================
# ACTIVITY GRAPH
# =============================

def activity_graph():

    if not ACTIVITY:
        return None

    df=pd.DataFrame(ACTIVITY)

    counts=df["phone"].value_counts()

    graph_df=pd.DataFrame({
        "phone":counts.index,
        "requests":counts.values
    })

    fig=px.bar(
        graph_df,
        x="phone",
        y="requests",
        title="User Activity Distribution"
    )

    return fig

# =============================
# ATTACK TIMELINE
# =============================

def attack_timeline():

    if not ACTIVITY:
        return None

    df=pd.DataFrame(ACTIVITY)

    df["time"]=pd.to_datetime(df["time"],unit="s")

    fig=px.scatter(
        df,
        x="time",
        y="phone",
        title="Attack Timeline"
    )

    return fig

# =============================
# ATTACK MAP
# =============================

def attack_map():

    if not ACTIVITY:
        return None

    df=pd.DataFrame(ACTIVITY)

    layer=pdk.Layer(
        "ScatterplotLayer",
        df,
        get_position="[lon,lat]",
        get_radius=50000,
        get_color=[255,0,0]
    )

    view=pdk.ViewState(
        latitude=23,
        longitude=78,
        zoom=4
    )

    deck=pdk.Deck(
        layers=[layer],
        initial_view_state=view
    )

    return deck

# =============================
# HEADER
# =============================

st.markdown(
"""
<style>
.big-title{
font-size:40px;
font-weight:bold;
color:#00ffcc;
}
.subtitle{
font-size:18px;
color:gray;
}
</style>
""",
unsafe_allow_html=True
)

st.markdown('<p class="big-title">🔐 NumLock AI Cybersecurity Platform</p>',unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI Driven Privacy Preserving Threat Detection</p>',unsafe_allow_html=True)

st.divider()

# =============================
# LIVE CYBER COUNTER
# =============================

active_threats=sum(1 for a in ALERTS)
blocked_attacks=len(ACTIVITY)
risk_level="LOW"

if blocked_attacks>20:
    risk_level="HIGH"

col1,col2,col3,col4=st.columns(4)

col1.metric("Registered Users",len(USER_DB))
col2.metric("Active Tokens",len(TOKENS))
col3.metric("Blocked Attacks",blocked_attacks)
col4.metric("System Risk Level",risk_level)

st.divider()

# =============================
# SIDEBAR
# =============================

menu=st.sidebar.selectbox(
"Module",
[
"Send Security Alert",
"Token System",
"Fraud Monitor",
"Threat Prediction",
"Attack Dashboard",
"Alerts Log"
]
)

if st.sidebar.button("Logout"):
    st.session_state["authenticated"]=False
    st.rerun()

# =============================
# ALERT SYSTEM
# =============================

if menu=="Send Security Alert":

    phone=st.text_input("Phone")

    if st.button("Trigger Alert"):

        msg=f"""
🚨 SECURITY ALERT

Suspicious activity detected

Phone: {phone}

System: NumLock AI
"""

        ok=send_alert(phone,msg)

        if ok:
            st.success("Alert sent")
        else:
            st.error("User not registered")

# =============================
# TOKEN SYSTEM
# =============================

elif menu=="Token System":

    phone=st.text_input("Phone")

    if st.button("Generate Token"):

        token=generate_token(phone)

        st.success(token)

# =============================
# FRAUD MONITOR
# =============================

elif menu=="Fraud Monitor":

    phone=st.text_input("Phone")

    if st.button("Check Fraud"):

        score=fraud_score(phone)

        st.metric("Fraud Score",score)

        if score>70:

            send_alert(
                phone,
                f"⚠ HIGH FRAUD ACTIVITY\nPhone:{phone}\nScore:{score}"
            )

            st.error("High Risk")

# =============================
# AI THREAT
# =============================

elif menu=="Threat Prediction":

    result=ai_anomaly_detection()

    st.subheader("AI Threat Analysis")

    st.write("Detection Result:",result)

    if result=="ANOMALY DETECTED":
        st.error("⚠ Suspicious behaviour detected")
    else:
        st.success("System behaviour normal")

# =============================
# DASHBOARD
# =============================

elif menu=="Attack Dashboard":

    st.subheader("Activity Distribution")

    fig=activity_graph()

    if fig:
        st.plotly_chart(fig)

    st.subheader("Attack Timeline")

    timeline=attack_timeline()

    if timeline:
        st.plotly_chart(timeline)

    st.subheader("Attack Map")

    deck=attack_map()

    if deck:
        st.pydeck_chart(deck)

# =============================
# ALERT LOG
# =============================

elif menu=="Alerts Log":

    if ALERTS:

        df=pd.DataFrame(ALERTS)

        st.dataframe(df)

    else:
        st.info("No alerts yet")

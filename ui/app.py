import streamlit as st
import requests
import hashlib
import time
import random
import pandas as pd
import plotly.express as px
import pydeck as pdk

# ======================
# CONFIG
# ======================

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# ======================
# DATABASE
# ======================

USER_DB = {}
TOKENS = {}
ACTIVITY = []
ALERTS = []

# ======================
# TELEGRAM REGISTRATION
# ======================

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

            if len(parts)==2:

                phone = parts[1]

                USER_DB[phone] = chat_id

# ======================
# TELEGRAM ALERT
# ======================

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

# ======================
# TOKEN SYSTEM
# ======================

def generate_token(phone):

    base = f"{phone}-{time.time()}"

    token = hashlib.sha256(base.encode()).hexdigest()[:16]

    TOKENS[token] = {
        "phone":phone,
        "exp":time.time()+300,
        "used":False
    }

    return token

# ======================
# FRAUD ENGINE
# ======================

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

# ======================
# AI THREAT PREDICTION
# ======================

def predict_threat():

    score=random.randint(0,100)

    if score<40:
        risk="LOW"
    elif score<70:
        risk="MEDIUM"
    else:
        risk="HIGH"

    return score,risk

# ======================
# ACTIVITY GRAPH
# ======================

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

# ======================
# ATTACK TIMELINE
# ======================

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

# ======================
# ATTACK MAP
# ======================

def attack_map():

    if not ACTIVITY:
        return None

    df=pd.DataFrame(ACTIVITY)

    layer=pdk.Layer(
        "ScatterplotLayer",
        df,
        get_position="[lon, lat]",
        get_radius=50000,
        get_color=[255,0,0],
    )

    view_state=pdk.ViewState(
        latitude=23,
        longitude=78,
        zoom=4
    )

    deck=pdk.Deck(
        layers=[layer],
        initial_view_state=view_state
    )

    return deck

# ======================
# STREAMLIT UI
# ======================

st.set_page_config(
    page_title="NumLock Security Center",
    layout="wide"
)

fetch_registrations()

st.title("🔐 NumLock AI Cyber Security Center")

# ======================
# SECURITY METRICS
# ======================

col1,col2,col3,col4=st.columns(4)

col1.metric("Registered Users",len(USER_DB))
col2.metric("Active Tokens",len(TOKENS))
col3.metric("Alerts Triggered",len(ALERTS))
col4.metric("Activity Events",len(ACTIVITY))

st.divider()

# ======================
# MENU
# ======================

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

# ======================
# ALERT
# ======================

if menu=="Send Security Alert":

    phone=st.text_input("Phone")

    if st.button("Trigger Alert"):

        msg=f"""
🚨 SECURITY ALERT

Suspicious activity detected

Phone: {phone}

System: NumLock
"""

        ok=send_alert(phone,msg)

        if ok:
            st.success("Alert Sent")
        else:
            st.error("User not registered")

# ======================
# TOKEN
# ======================

elif menu=="Token System":

    phone=st.text_input("Phone")

    if st.button("Generate Token"):

        token=generate_token(phone)

        st.success(token)

# ======================
# FRAUD
# ======================

elif menu=="Fraud Monitor":

    phone=st.text_input("Phone")

    if st.button("Check Fraud"):

        score=fraud_score(phone)

        st.metric("Fraud Score",score)

        if score>70:

            send_alert(
                phone,
                f"⚠️ HIGH FRAUD ACTIVITY\nPhone:{phone}\nScore:{score}"
            )

            st.error("High Risk")

# ======================
# THREAT
# ======================

elif menu=="Threat Prediction":

    score,risk=predict_threat()

    st.metric("Threat Score",score)

    st.write("Risk:",risk)

# ======================
# DASHBOARD
# ======================

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

# ======================
# ALERT LOG
# ======================

elif menu=="Alerts Log":

    if ALERTS:

        df=pd.DataFrame(ALERTS)

        st.dataframe(df)

    else:

        st.info("No alerts yet")

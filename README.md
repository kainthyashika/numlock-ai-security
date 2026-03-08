🔐 NumLock AI – Privacy-Preserving Cybersecurity Monitoring System

NumLock AI is an AI-driven cybersecurity monitoring platform designed to detect suspicious activities in real time while protecting user privacy through adaptive data disclosure and secure access control.

The system combines AI anomaly detection, fraud scoring, consent-based verification, tokenized access control, and honeypot defense mechanisms to provide a modern approach to privacy-preserving cybersecurity monitoring.

A live dashboard built with Streamlit enables administrators to visualize threats, monitor activity, and trigger real-time alerts.

---

🚀 Key Features

🤖 AI Threat Detection

Uses behavioral monitoring and anomaly detection techniques to identify suspicious or malicious activity.

🔐 Privacy-Preserving Data Access

Adaptive privacy protection dynamically masks sensitive data depending on the risk level detected by the system.

🎟 Tokenized Access Control

Short-lived security tokens ensure controlled access to sensitive resources.

📜 Consent Management System

Every access request is linked to a consent record and stored in a tamper-resistant ledger.

🕵️ Honeypot Defense

Suspicious users receive deceptive responses, helping identify malicious actors.

📱 Real-Time Security Alerts

Security alerts are sent instantly to users through Telegram bot notifications.

📊 Cybersecurity Dashboard

Interactive Streamlit dashboard showing:

- User activity distribution
- Fraud monitoring
- Threat prediction
- Security alerts
- Attack timeline
- Geographic activity map

🌐 Live Deployment

The system can be deployed on Streamlit Cloud and accessed through a web interface.

---

🧠 System Architecture

User Activity / Device Events
            ↓
Edge Monitoring Layer (Conceptual IoT Node)
            ↓
Activity Logging & Feature Extraction
            ↓
AI Anomaly Detection Engine
            ↓
Fraud Risk Scoring System
            ↓
Consent & Token Verification
            ↓
Adaptive Privacy Protection
            ↓
Honeypot Defense Module
            ↓
Alert Notification System
            ↓
Security Monitoring Dashboard

---

📊 Dashboard Capabilities

The NumLock AI dashboard provides a Security Operations Center (SOC) style interface including:

- Real-time security alerts
- Activity analytics
- Fraud monitoring
- AI threat prediction
- Attack timeline visualization
- Geographic attack map
- Alert logs

---

🛠 Technology Stack

Component| Technology
Backend| Python
AI / ML| Scikit-Learn
Data Processing| Pandas, NumPy
Visualization| Plotly
Dashboard| Streamlit
Notifications| Telegram Bot API
Mapping| PyDeck
Deployment| Streamlit Cloud
Version Control| Git & GitHub

---

📂 Project Structure

numlock-ai-security
│
├── ui
│   └── app.py                # Streamlit dashboard
│
├── src                      # Core security modules
│   ├── fraud_engine.py
│   ├── token_engine.py
│   ├── notifier.py
│   ├── prediction_model.py
│   ├── visualization.py
│   └── ledger.py
│
├── logs                     # Activity logs
├── models                   # AI models
│
├── requirements.txt
└── README.md

---

📱 Real-Time Alert Flow

1. User registers with the Telegram bot
2. Activity event is generated
3. AI system detects anomaly
4. Fraud score exceeds threshold
5. Honeypot or privacy guard activated
6. Alert notification sent to user device

---

🔬 Research Contribution

This project demonstrates a privacy-preserving cybersecurity monitoring architecture integrating:

- AI-driven behavioral analysis
- Adaptive privacy disclosure
- Token-based identity verification
- Honeypot deception techniques
- Real-time threat alerting

The system design supports potential integration with IoT edge monitoring devices such as ESP32 or Raspberry Pi, enabling distributed cybersecurity monitoring.

---

🌍 Live Demo

The system can be deployed using Streamlit Cloud, allowing the dashboard to be accessed through a public web link.

Example deployment:

https://numlock-ai-security.streamlit.app

---

📚 Future Improvements

- Federated AI threat detection
- Blockchain-based consent ledger
- Edge AI inference on IoT devices
- Mobile application interface
- Advanced attack prediction models

---

👩‍💻 Author

Yashika
Cybersecurity & AI Research Enthusiast

---

📜 License

This project is intended for academic and research purposes.

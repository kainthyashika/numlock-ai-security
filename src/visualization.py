import pandas as pd
import plotly.express as px

LOG_FILE = "../logs/activity.log"

def attack_graph():

    try:
        df = pd.read_csv(
            LOG_FILE,
            names=["time","phone","action","status"]
        )
    except:
        return None

    fig = px.histogram(
        df,
        x="phone",
        title="Activity Distribution by Phone"
    )

    return fig

from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 🔥 SENING NGROK LINKING
BOT_URL = "https://ruby-plantlike-unreligiously.ngrok-free.dev"

@app.route("/")
def home():
    try:
        data = requests.get(BOT_URL + "/api/stats").json()
    except:
        data = {"users": "X", "admins": "X", "auto": False}

    return f"""
    <h2>📊 Dashboard</h2>
    <p>👥 Users: {data['users']}</p>
    <p>👑 Admins: {data['admins']}</p>
    <p>🤖 Auto: {"ON" if data['auto'] else "OFF"}</p>

    <button onclick="toggle()">Toggle Auto</button>

    <script>
    function toggle(){{
        fetch('/toggle', {{method:'POST'}})
        .then(()=>location.reload())
    }}
    </script>
    """

@app.route("/toggle", methods=["POST"])
def toggle():
    try:
        requests.post(BOT_URL + "/api/toggle")
    except:
        pass
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

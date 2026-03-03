from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# test data (keyin bot bilan ulaymiz)
DATA = {
    "users": 120,
    "admins": 3,
    "auto": True
}

@app.route("/")
def home():
    return f"""
    <h2>📊 Dashboard</h2>
    <p>👥 Users: {DATA['users']}</p>
    <p>👑 Admins: {DATA['admins']}</p>
    <p>🤖 Auto: {"ON" if DATA['auto'] else "OFF"}</p>

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
    DATA["auto"] = not DATA["auto"]
    return "ok"

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

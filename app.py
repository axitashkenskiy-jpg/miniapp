from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

BOT_URL = "https://ruby-plantlike-unreligiously.ngrok-free.dev"

# 🔐 oddiy login (admin ID)
ADMIN_IDS = [8455026468]

def check_admin(user_id):
    return user_id in ADMIN_IDS

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form.get("user_id")

        if user_id and int(user_id) in ADMIN_IDS:
            return redirect(f"/dashboard?uid={user_id}")

        return "❌ Ruxsat yo‘q"

    return """
    <h2>🔐 Login</h2>
    <form method="post">
        <input name="user_id" placeholder="Telegram ID">
        <button>Login</button>
    </form>
    """

@app.route("/dashboard")
def dashboard():
    uid = request.args.get("uid")

    if not uid or int(uid) not in ADMIN_IDS:
        return "❌ Access denied"

    try:
        data = requests.get(BOT_URL + "/api/stats").json()
    except:
        data = {"users": "X", "admins": "X", "auto": False}

    return f"""
    <h2>📊 Dashboard</h2>

    <p>👥 Users: {data['users']}</p>
    <p>👑 Admins: {data['admins']}</p>
    <p>🤖 Auto: {"ON" if data['auto'] else "OFF"}</p>

    <form action="/toggle" method="post">
        <input type="hidden" name="uid" value="{uid}">
        <button>🤖 Toggle Auto</button>
    </form>

    <hr>

    <h3>📢 Broadcast</h3>
    <form action="/broadcast" method="post">
        <input type="hidden" name="uid" value="{uid}">
        <input name="text" placeholder="Xabar yoz...">
        <button>Yuborish</button>
    </form>
    """

@app.route("/toggle", methods=["POST"])
def toggle():
    uid = request.form.get("uid")

    if not uid or int(uid) not in ADMIN_IDS:
        return "❌"

    try:
        requests.post(BOT_URL + "/api/toggle")
    except:
        pass

    return redirect(f"/dashboard?uid={uid}")

@app.route("/broadcast", methods=["POST"])
def broadcast():
    uid = request.form.get("uid")

    if not uid or int(uid) not in ADMIN_IDS:
        return "❌"

    text = request.form.get("text")

    try:
        requests.post(BOT_URL + "/api/broadcast", json={"text": text})
    except:
        pass

    return redirect(f"/dashboard?uid={uid}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

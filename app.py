
from flask import Flask, jsonify
import psutil
import os
import time

app = Flask(__name__)

START_TIME = time.time()

@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Health Monitor",
        "version": "1.0",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/ready")
def readiness():
    return jsonify({
        "status": "ready"
    }), 200

@app.route("/metrics")
def metrics():

    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "process_id": os.getpid()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

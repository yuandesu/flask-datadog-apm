# app.py
from flask import Flask, jsonify
from ddtrace import patch_all, tracer
import requests
import time
from datetime import datetime

patch_all()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask with Datadog APM!"

@app.route("/check-datadog")
def check_datadog():
    # 只使用一個基本的 span
    with tracer.trace("check.datadog") as span:
        try:
            response = requests.get("https://www.datadoghq.com")
            return jsonify({
                'status': 'success',
                'status_code': response.status_code,
                'timestamp': datetime.now().isoformat()
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

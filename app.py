



from flask import Flask, jsonify, request
import random
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for testing

# Simulated threat types
THREAT_TYPES = ["Normal", "DDoS", "SQL Injection", "Malware", "Brute Force", "Phishing"]

# Store logs
logs = []

def generate_traffic():
    """Simulates live network traffic with predictions."""
    traffic_data = []

    for _ in range(10):  # Simulating 10 packets at a time
        threat = random.choice(THREAT_TYPES)
        confidence = round(random.uniform(0.5, 1.0), 2)  # Confidence between 50% and 100%
        intrusion_detected = "Intrusion Detected" if threat != "Normal" else "Safe"

        packet = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "traffic": intrusion_detected,
            "threat_type": threat,
            "confidence": confidence
        }

        # Log the event if intrusion detected
        if threat != "Normal":
            logs.append(packet)

        traffic_data.append(packet)

    return traffic_data

# @app.route("/", methods=["GET"])
# def home():
#     return jsonify({"status": "success", "message": "API is working!"}), 200
@app.route('/')
def home():
    return "Flask API is running!", 200



@app.route("/live_traffic", methods=["GET"])
def get_live_traffic():
    """Returns simulated live traffic data."""
    try:
        return jsonify({"status": "success", "results": generate_traffic()}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route('/send_alert', methods=['GET', 'POST'])
def send_alert():
    if request.method == 'GET':
        return jsonify({"status": "error", "message": "Use POST request for this endpoint"}), 405

    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"status": "error", "message": "Invalid request, 'message' field is required"}), 400

        alert = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "alert_message": data["message"]
        }

        logs.append(alert)
        return jsonify({"status": "success", "message": "Alert logged successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/chatbot", methods=["POST"])
def ai_chatbot():
    """Provides AI-driven security suggestions."""
    try:
        print("Request method:", request.method)  # Check if it's really POST
        print("Request headers:", request.headers)  # Debug request headers
        print("Received chatbot data:", request.get_json())  # Debugging

        if request.method != "POST":
            return jsonify({"status": "error", "message": "Only POST requests are allowed"}), 405

        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"status": "error", "message": "Invalid request, 'query' field is required"}), 400

        query = data.get("query", "").lower()

        response_map = {
            "ddos": "DDoS attacks flood the network, overloading servers. Mitigation: Rate limiting, firewall rules, and traffic filtering.",
            "sql injection": "SQL Injection attacks exploit database vulnerabilities. Use prepared statements and input validation to prevent them.",
            "malware": "Malware infections can be mitigated with antivirus software, firewalls, and regular security updates.",
            "brute force": "Brute force attacks try many password combinations. Prevent with account lockouts and strong password policies.",
            "phishing": "Phishing attempts steal sensitive data. Educate users and use email filtering solutions.",
            "normal": "No threats detected. Your network appears safe!"
        }

        best_match = next((key for key in response_map if key in query), None)

        if best_match:
            return jsonify({"status": "success", "response": response_map[best_match]}), 200
        else:
            return jsonify({"status": "error", "response": "I'm sorry, I didn't understand your query. Please ask about a specific threat type."}), 400

    except Exception as e:
        print("Error:", str(e))  # Debugging
        return jsonify({"status": "error", "message": str(e)}), 500



@app.route('/logs', methods=['GET'])
def get_logs():
    """Returns stored logs."""
    return jsonify({"status": "success", "logs": logs}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

APPOINTMENTS_FILE = "appointments.json"
user_sessions = {}  # Store temporary session data

# Load appointments from file
def load_appointments():
    if os.path.exists(APPOINTMENTS_FILE):
        with open(APPOINTMENTS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save appointments to file
def save_appointments(appointments):
    with open(APPOINTMENTS_FILE, "w") as file:
        json.dump(appointments, file, indent=4)

@app.route("/chat", methods=["POST"])
def chat():
    user_id = request.json.get("user_id", "default_user")
    user_message = request.json.get("message", "").strip()

    if user_id not in user_sessions:
        user_sessions[user_id] = {"step": 1}

    session = user_sessions[user_id]

    if session["step"] == 1:
        session["name"] = user_message
        session["step"] = 2
        return jsonify({"reply": "Got it! Can you also provide your location?"})

    elif session["step"] == 2:
        session["location"] = user_message
        session["step"] = 3
        return jsonify({"reply": "Thank you! Now, please provide the appointment date (YYYY-MM-DD)."})

    elif session["step"] == 3:
        session["date"] = user_message
        session["step"] = 4
        return jsonify({"reply": "Great! Now, enter the appointment time (HH:MM)."})
    
    elif session["step"] == 4:
        session["time"] = user_message
        appointment = {
            "name": session["name"],
            "location": session["location"],
            "date": session["date"],
            "time": session["time"]
        }

        appointments = load_appointments()
        appointments.append(appointment)
        save_appointments(appointments)

        session["step"] = 1  # Reset for next appointment
        return jsonify({"reply": f"✅ Appointment scheduled for {session['name']} on {session['date']} at {session['time']} in {session['location']}."})

    else:
        return jsonify({"reply": "I can help you schedule an appointment. What's your name?"})

@app.route("/appointments", methods=["GET"])
def get_appointments():
    appointments = load_appointments()
    return jsonify({"appointments": appointments})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

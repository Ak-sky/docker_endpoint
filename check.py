from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging to log to the console
logging.basicConfig(
    level=logging.DEBUG,  # Set log level to DEBUG for detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger()

# Simulated WiFi action
def trigger_wifi_action():
    # Replace with your actual WiFi handling logic
    logger.info("WiFi button triggered.")
    return "WiFi toggled successfully."

# API endpoint for WiFi button
@app.route('/trigger_wifi', methods=['POST'])
def trigger_wifi():
    if request.method == 'POST':
        # Log the trigger action
        action_response = trigger_wifi_action()
        
        # Log the request details (optional)
        logger.debug(f"Request received: {request.json}")
        
        return jsonify({"status": "success", "message": action_response}), 200
    else:
        logger.warning("Invalid request method.")
        return jsonify({"status": "error", "message": "Invalid request method."}), 405

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

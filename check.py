from flask import Flask, request, jsonify, render_template_string
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

# State variable to store the latest status
latest_status = {"message": "Ready", "hits": 0}

# Simulated WiFi action
def trigger_wifi_action():
    # Replace with your actual WiFi handling logic
    logger.info("WiFi button triggered.")
    return "WiFi toggled successfully."

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    logger.debug("Health check requested.")
    return jsonify({"status": "healthy"}), 200

# API endpoint for WiFi button
@app.route('/trigger_wifi', methods=['GET', 'POST'])
def trigger_wifi():
    global latest_status
    if request.method == 'POST':
        # Log the trigger action
        action_response = trigger_wifi_action()
        
        # Update the state variable
        latest_status["message"] = action_response
        latest_status["hits"] += 1
        
        logger.debug(f"Request received: {request.json}")
        return jsonify({"status": "success", "message": action_response}), 200
    elif request.method == 'GET':
        # Render an HTML page with the current status
        logger.info("Browser hit detected on /trigger_wifi.")
        return render_template_string(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Trigger WiFi</title>
            </head>
            <body>
                <h1>Trigger WiFi Endpoint</h1>
                <p>This endpoint toggles WiFi when accessed via POST.</p>
                <p><strong>Latest Status:</strong> {latest_status['message']}</p>
                <p><strong>Total Hits:</strong> {latest_status['hits']}</p>
            </body>
            </html>
        """)
    else:
        logger.warning("Invalid request method.")
        return jsonify({"status": "error", "message": "Invalid request method."}), 405

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

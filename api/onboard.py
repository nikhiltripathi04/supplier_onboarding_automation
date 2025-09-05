# api/onboard.py

from flask import Flask, request, jsonify
import logging
import requests 
import os

app = Flask(__name__)
logger = logging.getLogger(__name__)

def send_slack_notification(message: str):
    """Sends a message to a Slack channel using a webhook."""
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if not webhook_url:
        logger.warning("SLACK_WEBHOOK_URL environment not set.")
        return
    
    try: 
        payload = {'text': message}
        requests.post(webhook_url, json=payload)
        logger.info("Successfully sent Slack notification.")
    except Exception as e:
        logger.error(f"Failed to send Slack notification: {e}")

def validate_gstin_via_api(gstin: str) -> bool:
    """
    Simulates a call to an external API to validate a GSTIN.
    In a real-world scenario, you would replace this with a call to an actual
    GST validation service API.
    """
    logger.info(f"Pretending to validate GSTIN: {gstin}")
    # Placeholder Logic: For this example, we'll consider any GSTIN that
    # starts with '27' (for Maharashtra) as valid.
    if gstin and gstin.startswith('27'):
        # Here you would make the actual API call, e.g.:
        # response = requests.get(f"https://api.somegstservice.com/v1/verify?gstin={gstin}")
        # return response.json().get('isValid', False)
        return True
    else:
        return False

@app.route('/api/onboard', methods=['POST'])
def handle_onboarding():
    try:
        data = request.get_json()
        supplier_name = data.get('supplierName')
        gstin = data.get('gstin')

        if not all([supplier_name, gstin]):
            return jsonify({'message': "Error: supplierName and gstin are required."}), 400

        # --- New Validation Step ---
        is_valid = validate_gstin_via_api(gstin)

        if not is_valid:
            logger.warning(f"Validation FAILED for GSTIN: {gstin}")
            return jsonify({'message': f"Invalid GSTIN: {gstin}"}), 400
        
        # --- New Slack Notification ---
        logger.info(f"Validation PASSED for GSTIN: {gstin}")
        notification_message = f"New Supplier Ready for Approval:\nName: {supplier_name}\nGSTIN: {gstin}"
        send_slack_notification(notification_message)

        response_message = f"Successfully validated supplier: {supplier_name}"
        
        return jsonify({'message': response_message}), 200

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return jsonify({'message': "Internal Server Error."}), 500
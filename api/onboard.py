from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

# This single 'app' object will be discovered by Vercel
# Vercel routes requests to this file at the URL: /api/onboard
@app.route('/api/onboard', methods=['POST'])
def handle_onboarding():
    """
    This function handles the POST request to /api/onboard.
    """
    try:
        data = request.get_json()
        supplier_name = data.get('supplierName')

        if not supplier_name:
            logger.error("Validation Failed: 'supplierName' not found.")
            return jsonify({'message': "Error: 'supplierName' is a required field."}), 400
        
        # YOUR VALIDATION LOGIC WILL GO HERE ---
        # For now, we just log and return success.
        logger.info(f"Successfully processed data for: {supplier_name}")
        response_message = f"Vercel received data for supplier: {supplier_name}"

        return jsonify({'message': response_message}), 200
    
    except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return jsonify({'message': "An unexpected error occurred."}), 500
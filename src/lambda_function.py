import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Main handler for the Lambda function.
    Triggered by a POST request from API Gateway.
    """
    logger.info('RECEIVED EVENT')
    logger.info(event)

    try:
        # The form data comes in as a JSON string in the 'body'
        body = json.loads(event.get('body', '{}'))
        supplier_name = body.get('supplierName')

        if not supplier_name:
            logger.error("Validation Error: 'supplierName' not in request body.")
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({ 'message': "Error: 'supplierName is a required field."})
            }
        
        # This is where your validation and approval logic will go later.
        # For now, we just return a success message.
        logger.info(f"Successfully processed data for: {supplier_name}")

        response_message = f"Successfully received data for supplier: {supplier_name}"

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({ 'message': response_message })
        }
    
    except json.JSONDecodeError:
        logger.error("Execution failed: Invalid JSON in request body.")
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({ 'message': "Error: Invalid JSON in request body."})
        }
    
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({ 'message': "Internal Server Error."})
        }
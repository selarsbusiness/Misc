from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

app = Flask(__name__)
CORS(app)

# Configure Gemini API - Add your API key here
GEMINI_API_KEY = "AIzaSyDtx0tUqMEYbzQcCdfhQuyvIbAkSc9zDOg"
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Mapping of safety levels to HarmBlockThreshold
SAFETY_LEVELS = {
    "block_none": HarmBlockThreshold.BLOCK_NONE,
    "block_only_high": HarmBlockThreshold.BLOCK_ONLY_HIGH,
    "block_medium_and_above": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    "block_low_and_above": HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
}

# Harm categories
HARM_CATEGORIES = {
    "harassment": HarmCategory.HARM_CATEGORY_HARASSMENT,
    "hate_speech": HarmCategory.HARM_CATEGORY_HATE_SPEECH,
    "sexually_explicit": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
    "dangerous_content": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT
}


# Client function that calls Google Gemini API
def client_function(user_input: str, safety_settings: dict = None) -> str:
    """
    Sends user input to Google Gemini API and returns the response.
    
    Args:
        user_input: The user's input text
        safety_settings: Dict with format {
            "harassment": "block_level",
            "hate_speech": "block_level",
            "sexually_explicit": "block_level",
            "dangerous_content": "block_level"
        }
    """
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured. Please add your API key.")
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Build safety settings if provided
        safety_settings_list = []
        if safety_settings:
            for category_name, level_name in safety_settings.items():
                if category_name in HARM_CATEGORIES and level_name in SAFETY_LEVELS:
                    safety_settings_list.append({
                        "category": HARM_CATEGORIES[category_name],
                        "threshold": SAFETY_LEVELS[level_name]
                    })
        
        # Generate content with safety settings
        if safety_settings_list:
            response = model.generate_content(user_input, safety_settings=safety_settings_list)
        else:
            response = model.generate_content(user_input)
        
        return response.text
    except Exception as e:
        raise Exception(f"Gemini API error: {str(e)}")


# Stubbed out API client function
def api_client_function(processed_data: str) -> str:
    """
    Takes processed data and makes an API call.
    This is a stub that you can replace with actual API logic.
    """
    # Placeholder implementation
    return f"API Result: {processed_data} - [API Response]"


@app.route('/api/process', methods=['POST'])
def process_input():
    """
    Endpoint to process user input through the client function.
    Accepts optional safety_settings parameter.
    """
    try:
        data = request.get_json()
        user_input = data.get('input', '')
        safety_settings = data.get('safety_settings', None)
        
        if not user_input:
            return jsonify({'error': 'Input is required'}), 400
        
        result = client_function(user_input, safety_settings)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/call', methods=['POST'])
def call_api():
    """
    Endpoint to trigger the API client function with processed data.
    """
    try:
        data = request.get_json()
        processed_data = data.get('data', '')
        
        if not processed_data:
            return jsonify({'error': 'Data is required'}), 400
        
        result = api_client_function(processed_data)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)

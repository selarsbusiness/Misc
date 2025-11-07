# Python Web Application

A simple web application with a Python Flask backend and modern frontend that processes user input through stubbed client and API functions.

## Project Structure

```
PythonWebApp/
├── app.py              # Flask backend with API endpoints
├── index.html          # Frontend UI
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Setup Instructions

### 1. Set Up Gemini API Key

This application uses the Google Gemini API to generate song lyrics. You'll need to:

1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Set the `GEMINI_API_KEY` environment variable:

**On Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY = "your-api-key-here"
```

**On Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**On macOS/Linux:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 4. Open the Frontend

Open `index.html` in your web browser or serve it through a local web server:

```bash
# Using Python's built-in server (from the project directory)
python -m http.server 8000
```

Then navigate to `http://localhost:8000`

## Features

- **User Input Field**: Enter text to process
- **Process Button**: Sends input to the `client_function()` stub
- **Processed Output**: Read-only field displaying the result
- **API Call Button**: Triggers the `api_client_function()` stub with the processed data
- **API Result**: Read-only field displaying the API response
- **Status Messages**: Real-time feedback on operations

## Customization

### Modify the Client Function

Edit the `client_function()` in `app.py` to implement your actual processing logic:

```python
def client_function(user_input: str) -> str:
    # Replace this with your actual implementation
    return f"Processed: {user_input.upper()}"
```

### Modify the API Client Function

Edit the `api_client_function()` in `app.py` to implement your actual API logic:

```python
def api_client_function(processed_data: str) -> str:
    # Replace this with your actual API calls
    return f"API Result: {processed_data} - [API Response]"
```

## API Endpoints

### POST /api/process
Processes user input through the client function.

**Request:**
```json
{
  "input": "user text"
}
```

**Response:**
```json
{
  "result": "Processed: USER TEXT"
}
```

### POST /api/call
Triggers the API client function with processed data.

**Request:**
```json
{
  "data": "processed data"
}
```

**Response:**
```json
{
  "result": "API Result: processed data - [API Response]"
}
```

## Notes

- The frontend uses CORS to communicate with the Flask backend
- Both functions are currently stubbed out with placeholder implementations
- The UI is built with modern CSS and vanilla JavaScript
- Status messages provide real-time feedback on all operations

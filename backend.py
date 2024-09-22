from flask import Flask, request, jsonify
import base64

app = Flask(_name_)

# Helper function to filter data for POST request
def filter_data(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha() and item.islower()]
    highest_lowercase = max(alphabets) if alphabets else None
    return numbers, alphabets, highest_lowercase

# POST method for processing JSON data
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Get the JSON data from the request
        req_data = request.get_json()

        # Validate input JSON
        if 'data' not in req_data or 'file_b64' not in req_data:
            return jsonify({"is_success": False, "message": "Invalid input format"})

        data = req_data['data']
        file_b64 = req_data['file_b64']

        # Decode base64 file
        try:
            file_data = base64.b64decode(file_b64)
        except Exception as e:
            return jsonify({"is_success": False, "message": "Invalid base64 encoding"})

        # Process the data (numbers, alphabets, highest lowercase alphabet)
        numbers, alphabets, highest_lowercase = filter_data(data)

        # Return the desired response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABC0123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase,
            "file_valid": True,
            "file_mime_type": "image/png",  # Assuming file type from base64
            "file_size_kb": str(len(file_data) // 1024)  # Size of file in KB
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)})

# GET method for basic information about the API
@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    # Hardcoded response for the GET request
    response = {
        "operation_code": 1
    }
    
    return jsonify(response), 200

if _name_ == '_main_':
    app.run(debug=True)

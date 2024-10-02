from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # Renders the HTML form

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Get JSON data from the request
    
    # Define the path for the JSON file
    json_file_path = 'data.json'

    # Check if the file exists
    if os.path.exists(json_file_path):
        # If it exists, read the existing data
        with open(json_file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []  # If not, create an empty list

    # Append new data
    existing_data.append(data)

    # Write updated data to the JSON file
    with open(json_file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

    return jsonify({'message': 'Data saved successfully!'})

if __name__ == '__main__':
    app.run(debug=True)

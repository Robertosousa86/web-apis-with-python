from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# app.run(debug=True)

# Define what the app does
@app.get("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    if not first_name and not last_name:
        return jsonify({'status': 'error'})
    elif first_name and not last_name:
        response = {'data': f'Hello {first_name}!!!!!'}
    elif not first_name and last_name:
        response = {'data': f'Hello {last_name}!'}
    else:
        response = {'data': f'Is your name {first_name} {last_name}'}

    return jsonify(response)

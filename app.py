from flask import Flask, request, jsonify
from cameraTest import letsDoIt

app = Flask(__name__)

@app.route('/prime', methods=['POST'])
def prime():
    """Endpoint to process incoming requests. 
    (POST requests with JSON mapping 'obj' to command)"""
    trigger(None)
    return jsonify({"SUCCESS":True})


def trigger(command_string):
    """Uses token-matching to act on a command.
    command_string  : str, Command. For example : "fan off", "turn the light on", etc.
    status          : str (optional), Turns port ON if status is 'on'. Else turns port OFF.
    """
    # Convert command to lower case and split into words
    command_words = set(command_string.lower().split(" "))
    # Set status to 'on' if the word 'on' is present in the command (command_words)
    # Iterate over all appliances (ie. keys in words)
    print("this shoudl be working")
    letsDoIt()


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=8000)
    print("fucking test")
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def ussd_handler():
    """
        USSD Requests Handler, usage:
        CON - Response requiring Input
        END - Response ending USSD Session
    """

    if request.method == 'GET':
        return "Hey there, I process majorly POST requests from Africa's Talking USSD"

    elif request.method == 'POST':
        # Gets the POST Request Data
        request_data = request.form
        session_id = request_data['sessionId']
        service_code = request_data['serviceCode']
        phone_number = request_data['phoneNumber']
        ussdTextList = request_data['text'].split('*')


        # Send a response to user
        return "CON Welcome to my USSD Application!"

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=8080)
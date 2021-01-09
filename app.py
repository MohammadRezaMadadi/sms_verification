from flask import Flask, jsonify, request
app = Flask(__name__)


@app.rout('/Ver1/recive_sms', methods=[post])
def recive_sms():
    '''function to recive customer's message'''
    data = request.form
    sndr = data['from']
    msg = data['message']
    print(f'We recived: {msg} from: {sndr}')
    return jsonify(msg), 200

def send_sms():
    '''function to send verification to customer'''
    pass

def chk_serial():
    '''function to check serial number sent from customer'''
    pass

if __name__ == '__main__':
    app.run('0.0.0.0',5000, debug= True)



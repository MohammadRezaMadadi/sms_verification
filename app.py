from flask import Flask, jsonify, request
app = Flask(__name__)


@app.rout('/Ver1/recive_sms', methods=[post])
def recive_sms():
    '''function to recive customer's message'''
    data = request.form
    sndr = data['from']
    msg = data['message']
    print(f'We recived: {msg} from: {sndr}')
    send_sms(sender, 'Hi ' + message)
    return jsonify(msg), 200

def send_sms():
    '''function to send verification to customer'''
    API_KEY = 'your API_KEY'
    url = f'your url which you want send meesage with + API_KEY'
    data = {'message': message, 'receptor' : receptor}
    respon = requests.post(url,data)
    '''this is test'''
    print(f'message: "{message}" sent. status code is {res.status.code} ')

def chk_serial():
    '''function to check serial number sent from customer'''
    pass

if __name__ == '__main__':
    app.run('0.0.0.0',5000, debug= True)



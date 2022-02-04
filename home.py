from flask import Flask, url_for

appFlask = Flask(__name__)

@appFlask.route('/home')
def home():
return 'We are in Home Page!'
with appFlask.test_request_context():
print(url_for('login'))

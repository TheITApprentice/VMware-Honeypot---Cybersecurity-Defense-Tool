from flask import Flask, request, render_template, jsonify, redirect
import logging
from datetime import datetime

app = Flask(__name__)

# Set up basic logging configuration
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to log attempts
def log_attempt(endpoint, method, data=None, ip=None, user_agent=None):
    log_entry = {
        'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'endpoint': endpoint,
        'method': method,
        'ip': ip or request.remote_addr,
        'user_agent': user_agent or request.headers.get('User-Agent'),
        'data': data
    }
    logging.info('Attempt Detected: %s', log_entry)

# Redirect root to the VMware UI
@app.route('/', methods=['GET'])
def redirect_to_vmware_ui():
    return redirect('/ui/', code=302)

# Simulate VMware HTTPS service on port 443
@app.route('/ui/', methods=['GET', 'POST'])
def vsphere_ui():
    if request.method == 'POST':
        # Log the attempt with dummy credentials
        log_attempt('/ui/', 'POST', request.form)
        return jsonify({'message': 'Login failed'}), 401
    else:
        # Display a dummy login page
        log_attempt('/ui/', 'GET')
        return render_template('dummy_vsphere_login.html')

# Error handler for 404 to simulate scanning activity
@app.errorhandler(404)
def page_not_found(e):
    log_attempt('404_error', request.method)
    return jsonify({'message': 'Service not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

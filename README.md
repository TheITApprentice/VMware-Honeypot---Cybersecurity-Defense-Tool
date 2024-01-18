🌐 VMware Honeypot (Python Flask) 🚀
** Cyber Security - Blue Team - Honeypot for VMware (on-prem)**

[Quick Start Guide for VMware Honeypot]
Welcome to our VMware Honeypot – a simple yet effective tool to gather insights into potential cyber threats targeting VMware environments. Follow these steps to set up the honeypot and enhance your understanding of attack vectors.

🌟 Features:
Realistic Interface: Inspired by the vSphere Web Client, our honeypot offers a basic yet convincing environment for potential attackers.
Basic Interaction: The honeypot interacts with users through simulated endpoints, capturing minimal data such as IP addresses and timestamps.
Flask Python Backend: Powered by Flask, the Python web framework, the backend of the honeypot simulates basic endpoints.
Security Measures: The honeypot is designed with isolation and monitoring to prevent any potential risks.
Analysis and Reporting: Collected data can be analyzed periodically for basic insights into attack methods.

🛠️ Prerequisites:
A Linux/Windows desktop or server to host the honeypot.
Basic knowledge of web development (HTML, CSS, JavaScript).
Flask Python web framework for backend simulation.

[Setup Steps:]
1) Clone the Repository: Start by cloning our GitHub repository containing the VMware Honeypot code.

2) Configure Flask Backend:
- Install Flask and other required dependencies using:
pip install flask

3) Run the Honeypot
   -Navigate to the project directory
   cd VMware_honeypot

4) Run the Honeypot:
   - python vmware.py
  
🚀 Usage:
Once executed, ensure the server is running. Visit http://localhost:5000 - you will be redirected to the dummy VMWare Sphere single sign-on page /ui/.

Here, when somebody attempts to log in, a message will be logged into honeypot.log with relevant information.

📊 Analysis:
Periodically review the honeypot.log file for insights into potential attack methods.
Analyze IP addresses, timestamps, and any captured data to understand trends.

🙌 Credits:
We appreciate the community support for feedback and improvement. Feel free to share your thoughts on our GitHub repository.

🎭 Mike Foley Humour: Utilizing some templating from Mike Foley Themes for comedic effect! 😄 #VMwareHoneypot #CyberSecurity #FlaskTutorial

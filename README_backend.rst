===========
Back-end example setup
===========

Create and environment with python=3.6 and install requirements from 'backend_requirements.txt'
Run 'pyhton backend.py' and navigate to  "http://127.0.0.1:5000/"
Check the OIDC .well-known document at "http://127.0.0.1:5000/credentials/oidc"
Go to "http://127.0.0.1:5000/me": an error will be prompted since a token is missing from the request

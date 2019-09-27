import os
import json

from flask import Flask, request, redirect

import requests
import jwt
from jwksutils import rsa_pem_from_jwk

app = Flask(__name__)

os.environ['OIDC_SERVER'] = "https://accounts.google.com/.well-known/openid-configuration"


@app.route('/')
def hello_world():
    return json.dumps({'hello': 'Welcome anonymous.'})
    

@app.route('/credentials/oidc')
def expose_well_known_oidc():
    return redirect(os.environ['OIDC_SERVER'])


@app.route('/me')
def get_user_info():
    try:
        bearer = request.headers['Authorization'].replace('Bearer ','')
        user_id = None
        if bearer:
            bearer_decoded = verify_token(bearer)
            out_msg = 'Welcome %s' % bearer_decoded['email']
    except:
        out_msg = 'Something went wrong, token missing or invalid.'
    
    return json.dumps({'hello': out_msg})



def verify_token(token):
    
    # Decode token to get issuer url
    token_header = jwt.get_unverified_header(token)
    token_unverified = jwt.decode(token, verify=False)
    
    response = requests.get(os.environ['OIDC_SERVER'])
    if response.status_code == 200:
        issuer = response.json()['issuer']
    
    token_verified = None
    if issuer == token_unverified['iss']:
        # Get public key from IP
        # NB: these keys can be cached, depending how often the Identity Provider is refreshing them
        jwks = get_auth_jwks(os.environ['OIDC_SERVER'])
        for key in jwks['keys']:
            if key['kid'] == token_header['kid']:
                public_key = rsa_pem_from_jwk(key)
        
        token_verified = jwt.decode(token,
                             public_key,
                             verify=True,
                             algorithms=token_header['alg'],
                             audience=token_unverified['azp'],
                             issuer=token_unverified['iss'])
        
    return token_verified
    

def get_auth_jwks(oidc_well_known_url):
    
    jwks = None    
    response = requests.get(oidc_well_known_url)
    if response.status_code == 200:
        jwks_uri = response.json()['jwks_uri']
        response = requests.get(jwks_uri)
        if response.status_code == 200:
            jwks = response.json()
    
    return jwks
    

if __name__ == '__main__':
    app.run()

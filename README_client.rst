===========
Client example setup
===========

For this example Postman will be the openEO client (See client_postman.png).

- Open Postman
- Insert the url of your back-end's protected endpoint ("http://127.0.0.1:5000/me") as a GET request
- Under Authorization select OAuth2.0 and click on "Get New Access Token" (although we need an id_token, so we'll need a small hack)
- Select "Authorization Code" as Grant Type
- Fill in the Auth and Access Token URLs as specified under "http://127.0.0.1:5000/credentials/oidc"
- Fill the client_id, client_password and callback url with the fields you got when registering your application in the Identity Provider (see README_user.rst)
- Fill the Scope as "openid email" (In general, you can check which scopes are available from the IP on the .well-known)
- Click Request Token

Postman will open a pop-up window where you can insert your Identity Provider's credentials (in the example we are using Google). Make sure that the callback url is IDENTICAL to the one you have registered on your application when setting it up (see README_user.rst)

- Copy the id_token to the clipboard and click on "Use Token", then copy the id_token in the "Access Token" field.
- Select "Request Headers" under "Add authorization data to" on the left panel (See client_postman.png)
- Send the request, if all goes well, you will see a welcome message with your email.

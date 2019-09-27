===========
User example setup
===========

A user needs to register his/her (openEO) application with the Identity Provider supported by the back-end and visible at the endpoint "/credentials/oidc". this means obtaining the following three fields:

- client_id
- client_password
- redirect_uri (also called callback_uri). One application may have multiple redirect_uris.

Depending on the IP, this is something that the user may or may not be able to do on their own. In this example we are using Google as IP so a user can do this procedure independently. Otherwise the user needs to ask the IP/back-end to provide the fields above.

- For this example you need to have a Google account
- Got to "https://console.developers.google.com" and log in
- Under Credentials click on "Create Credentials" and select "OAuth client ID"
- Select "Web application" and give a nme to your app, e.g. <my_name>-openEO
- Add "http://localhost:5000/oidc_callback" under "Authorized redirect URIs". The URL could be something else, but this needs some extra steps.
For example, if you want "https://my-website.com/oidc/callback" as redirect, you need to add "https://my-website.com" under "Authorized JavaScript origins", 
which in turn requires you to add "my-website.com" under "Authorized domains" in the "OAuth Consent Screen" page (left panel).

Once saved, you will have obtained a client_id/client_secret/callback_url that you can use from the client (see README_client.rst)

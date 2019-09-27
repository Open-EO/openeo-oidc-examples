===========
openeo-oidc-examples
===========

This repository describes the logical flow of using OpenIDConnect (OIDC) for openEO and includes an example using a simple python-based back-end, Postman as a client and Google as identity provider.


Logical steps 
============

There are four entities involved in openEO OIDC-based authentication: user, identity provider (IP), openEO client (client), openEO back-end (back-end).
The goal is to be able to authenticate users without the client and back-end ever have to directly deal with user credentials. For this to work, each entity has a role:

- user (see README_user.rst):
  - register an application at the IP supported by the back-end (the user can find this at /credentials/oidc). The user obtains from the IP a client_id/client_secret for his/her application and needs to set one or more redirect URIs.
- back-end (see README_backend.rst): 
  - exposes the supported IP on /credentials/oidc. This is a .well-known OIDC document listing the IP endpoints for authorization, tokens, etc ... The supported IP may or may not be directly managed by the group maintaining the back-end.
  - upon requests on protected endpoints, the back-end:
    - verifies the presence and validity of the token (this is done by getting the WJT keys from the IP keys endpoint available on the .well-known OIDC document)
    - decode the token if valid
- client (see README_client.rst): given the .well-known OIDC document exposed by the back-end, request an id_token from the supported IP. A pop up at the redicrect_url specified by the user in its application will prompt the user to type in his/her credentials. Upon receiving the id_token, the client send the request to the back-end with this token embedded in the header.
- IP: issues an id_token for a correct request. The IP may or may not be directly managed by the group maintaining the back-end, in this example Google is used.

# Token Authentication

User requests access to the server giving there account info and password. The server side would generate
a token to the user. In the following visit, until the token expires, user would be able to visit the
website with the token.

> Token-based authentication is a protocol that generates encrypted security tokens. 
> It enables users to verify their identity to websites, which then generates a unique encrypted 
> authentication token.
 
## Steps

- **Request**: The user logs in to a service using their login credentials, which issues an access request to a server or protected resource.
- **Verification**: The server verifies the login information to determine that the user should have access. This involves checking the password entered against the username provided.
- **Token submission**: The server generates a secure, signed authentication token for the user for a specific period of time.
- **Storage**: The token is transmitted back to the user’s browser, which stores it for access to future website visits. When the user moves on to access a new website, the authentication token is decoded and verified. If there is a match, the user will be allowed to proceed.
- **Expiration**: The token will remain active until the user logs out or closes the server.

import os
from security_module.token_validation import verify_jwt
from typing import List
## try to read AUTH0_DOMAIN from environment variables if not found raise an exception




def auth_validator(token: str, audience: List[str], auth0_domain: str) -> dict:
    """
    Validate the authorization token

    Args:
        token string: The JWT token to be verified.
        audience list: The audience of the token.
        auth0_domain string: The Auth0 domain.

    Returns:
        dict: The claims from the verified JWT token.

    Raises:
        Exception: If the token is expired or verification fails
    """
    
    claims = verify_jwt(token, audience, auth0_domain)
    if not claims:
        raise Exception("Unauthorized no claims found")
    return claims


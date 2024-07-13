from _http import HttpRequest
import jwt
import os, requests, json
from jose.exceptions import ExpiredSignatureError
from jwt.algorithms import RSAAlgorithm

## try to read AUTH0_DOMAIN from environment variables if not found raise an exception

ALGORITHMS = ["RS256"]
AUDIENCE = os.getenv('AUDIENCE') or "PLACEHOLDER"
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
if not AUTH0_DOMAIN:
    raise Exception("AUTH0_DOMAIN environment variable not found")

def auth_validator(req: HttpRequest):
    """
    Validate the authorization token in the HTTP request.

    Args:
        req (HttpRequest): The incoming HTTP request object containing headers.

    Returns:
        dict: The claims from the verified JWT token.

    Raises:
        Exception: If the Authorization header is missing or if the token is invalid.
    """
    auth_header = req.headers.get('Authorization')
    if not auth_header:
        raise Exception("Missing Authorization header")
    token = auth_header.split(" ")[1]
    claims = verify_jwt(token)
    
    if not claims:
        raise Exception("Unauthorized no claims found")
    return claims

def get_jwks():
    """
    Fetch the JSON Web Key Set (JWKS) from the Auth0 domain.

    Returns:
        dict: The JWKS containing public keys.
    """
    jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
    response = requests.get(jwks_url)
    return response.json()

def verify_jwt(token):
    """
    Verify the JWT token using the public keys from the JWKS.

    Args:
        token (str): The JWT token to be verified.

    Returns:
        dict: The claims from the verified JWT token.

    Raises:
        Exception: If the token is expired or verification fails.
    """
    try:
        jwks = get_jwks()
        unverified_header = jwt.get_unverified_header(token)
        public_keys = {}
        for key in jwks['keys']:
            kid = key['kid']
            public_key = RSAAlgorithm.from_jwk(json.dumps(key))
            public_keys[kid] = public_key
        # Extract the kid from the token header
        kid = unverified_header['kid']
        if kid in public_keys:
            claims = jwt.decode(token, key=public_keys[kid], algorithms=ALGORITHMS, audience=AUDIENCE, issuer=f"https://{AUTH0_DOMAIN}/")
            return claims
        
    except ExpiredSignatureError:
        raise Exception("Unauthorized token has expired")
    except Exception as e:
        raise Exception("Unauthorized token verification failed")

from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt

from core.config import settings  # Ensure this is correctly defined in your project

def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Generate a JWT access token.

    Args:
        data (dict): The payload to encode in the JWT.
        expires_delta (Optional[timedelta]): Custom expiration time for the token.

    Returns:
        str: The encoded JWT.
    """
    # Copy the input data to avoid mutation
    to_encode = data.copy()

    # Set expiration time
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    # Encode the token
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    
    return encoded_jwt

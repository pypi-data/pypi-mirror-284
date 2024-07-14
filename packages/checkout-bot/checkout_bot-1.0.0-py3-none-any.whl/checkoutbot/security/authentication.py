import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def validate_api_key(provided_key):
    """
    Validates the provided API key.
    
    Args:
        provided_key (str): The API key to validate.
    
    Returns:
        bool: True if the API key is valid, False otherwise.
    """
    return provided_key == API_KEY

def authenticate_user(username, password):
    """
    Authenticates a user with a username and password.
    
    Args:
        username (str): The username.
        password (str): The password.
    
    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    # Implement user authentication logic (e.g., check against a database)
    # For demo purposes, we use hardcoded values
    return username == "admin" and password == "password"

# Example usage
# print(validate_api_key("your-provided-api-key"))
# print(authenticate_user("admin", "password"))

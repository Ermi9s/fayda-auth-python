import requests
import logging
import jwt

def fetch_user_info_from_fayda(access_token: str, user_info_url: str) -> dict:
    response = requests.get(user_info_url, headers={"Authorization": f"Bearer {access_token}"}, verify=False)
    if response.status_code != 200:
        logging.error(f"User info request failed: {response.status_code}")
        raise Exception(f"Unexpected status code: {response.status_code}")
    
    token = response.text
    return jwt.decode(token, options={"verify_signature": False})
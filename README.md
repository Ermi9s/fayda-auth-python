# Fayda Auth Python Library

`fayda-auth` is a Python library for integrating with Fayda Esignet OAuth authentication. It simplifies the process of generating authorization URLs, managing sessions with Redis, and authenticating users via token exchange, supporting modern JWK-based client assertions.

---

## Features

- Generate OAuth authorization URLs for Fayda Esignet.
- Secure session management using Redis.
- Client assertion generation with JWK private keys.
- Easy integration with Python applications (e.g., Flask, django, etc..).

---

## Installation

Install `fayda-auth` from PyPI:

```bash
pip install fayda-auth
```

### Requirements

- Python 3.8 or higher
- A running Redis server

---

## Quick Start

Here’s a basic example to get started:

```python
from fayda_auth import FaydaAuth, HostConfig
import redis

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Configure FaydaAuth
auth = FaydaAuth(
    host_configs=[HostConfig(origin="http://localhost:3000", redirect_uri="http://localhost:3000/callback")],
    redis_client=redis_client,
    env_file=".env"
)

# Generate authorization URL
result = auth.authorize("http://localhost:3000")
print(result)

# Authenticate (example with mock data)
auth_result = auth.authenticate(
    session_id=result["data"]["session_id"],
    auth_code="mock_auth_code",
    csrf_token=result["data"]["state"]
)
print(auth_result)
```

---

## Configuration

Create a `.env` file in your project root with the following variables:

```plaintext
REDIS_HOST=localhost
REDIS_PORT=6379
FAYDA_OAUTH_CLIENT_ID=your_client_id
FAYDA_OAUTH_CLIENT_ASSERTION_TYPE=urn:ietf:params:oauth:client-assertion-type:jwt-bearer
FAYDA_OAUTH_PRIVATE_KEY=<base64_encoded_jwk_private_key>
FAYDA_AUTHORIZE_URL=https://esignet.example.com/authorize
FAYDA_TOKEN_URL=https://esignet.example.com/v1/esignet/oauth/v2/token
FAYDA_USER_INFO_URL=https://esignet.example.com/v1/esignet/oidc/userinfo
```

### Notes

- `FAYDA_OAUTH_PRIVATE_KEY` must be a base64-encoded JWK (JSON Web Key) RSA private key.
- Replace placeholders (e.g., `your_client_id`) with actual values from Fayda Esignet.

---

## Usage with Flask

For a complete example with Flask, see the sample app below:

```python
from flask import Flask, request, jsonify
from fayda_auth import FaydaAuth, HostConfig
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=0)
auth = FaydaAuth(
    host_configs=[HostConfig("http://localhost:3000", "http://localhost:3000/callback")],
    redis_client=redis_client,
    env_file=".env"
)

@app.route('/authorize', methods=['GET'])
def authorize():
    origin = request.args.get('utm_source', 'http://localhost:3000')
    try:
        result = auth.authorize(origin)
        return jsonify(result), result['status_code']
    except Exception as e:
        return jsonify({"error_message": str(e), "status_code": 500}), 500

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    try:
        result = auth.authenticate(
            session_id=data['session_id'],
            auth_code=data['auth_code'],
            csrf_token=data['csrf_token']
        )
        return jsonify(result), result['status_code']
    except Exception as e:
        return jsonify({"error_message": str(e), "status_code": 500}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
```

Run it:

```bash
python app.py
```

Test endpoints:

- Authorize

```json
curl "http://localhost:5252/authorize?utm_source=http://localhost:3000"

Response

{
    "message": "",
    "data": {
        "auth_url": "",
        "session_id": "",
        "utm_referer": "",
        "utm_source": ""
    },
    "status_code": 200
}
```

- Authenticate
  - ```json
    curl -X POST http://localhost:5252/authenticate -H "Content-Type: application/json" -d '{"session_id": "<session_id>", "auth_code": "mock_auth_code", "csrf_token": "<state>"}'

    Request Body

    {
        "session_id":"V2IQ58T72qx5HMatkV78aVDBtwNIVLvb",
        "auth_code":"ZUlqAjzTwDhOFc5erg7V6BrPfeRAYShMiOdnRBC88eY",
        "csrf_token":"9Uc0Ibzo80VNDtPSNEQjwQu8"
    }

    Response Body

    {
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "properties": {
                    "address": {
                        "type": "object",
                        "properties": {
                            "kebele": {
                                "type": "string"
                            },
                            "region": {
                                "type": "string"
                            },
                            "woreda": {
                                "type": "string"
                            },
                            "zone": {
                                "type": "string"
                            }
                        }
                    },
                    "birthdate": {
                        "type": "string"
                    },
                    "gender": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "phone": {
                        "type": "string"
                    },
                    "picture": {
                        "type": "string"
                    },
                    "residenceStatus": {
                        "type": "string"
                    },
                    "sub": {
                        "type": "string"
                    }
                }
            },
            "status_code": {
                "type": "integer"
            }
        }
    }
    ```

    ```

    ```

---

## Dependencies

- `redis`
- `python-dotenv`
- `pyjwt`
- `cryptography`
- `requests`
- `jwcrypto` (for JWK support)

Install them with:

```bash
pip install -r requirements.txt
```

---

## Development

### Running Tests

```bash
pip install pytest pytest-cov
pytest --cov=fayda_auth tests/
```

### Code Style

```bash
pip install flake8 black
flake8 fayda_auth/
black fayda_auth/
```

---

## Contributing

1. Fork the repository:
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Developed By

 **[Awura Computing PLC](https://awura.tech/ "Awura Computing PLC")** , **Addis Ababa, Ethiopia**

from typing import Dict, Optional, Any, Union, List
from .handlers.fayda import FaydaOAuthHandler
from .config.redis import RedisConfig
from .config.hosts import HostConfigManager, HostConfig
from .exceptions import FaydaAuthError

class FaydaAuth:
    def __init__(
        self,
        redis_client=None,
        env_file: Optional[str] = None,
        client_id: Optional[str] = None,
        authorize_url: Optional[str] = None,
        token_url: Optional[str] = None,
        user_info_url: Optional[str] = None,
        private_key: Optional[str] = None,
        client_assertion_type: Optional[str] = None,
        host_configs: Optional[Union[Dict[str, str], List[HostConfig]]] = None
    ):
        """Initialize the FaydaAuth library."""
        from dotenv import load_dotenv
        import os
        
        if env_file:
            load_dotenv(env_file)
        
        self.client_id = client_id or os.getenv("FAYDA_OAUTH_CLIENT_ID")
        self.authorize_url = authorize_url or os.getenv("FAYDA_AUTHORIZE_URL")
        self.token_url = token_url or os.getenv("FAYDA_TOKEN_URL")
        self.user_info_url = user_info_url or os.getenv("FAYDA_USER_INFO_URL")
        self.private_key = private_key or os.getenv("FAYDA_OAUTH_PRIVATE_KEY")
        self.client_assertion_type = client_assertion_type or os.getenv("FAYDA_OAUTH_CLIENT_ASSERTION_TYPE")
        
        if not all([self.client_id, self.authorize_url, self.token_url, self.user_info_url, self.private_key]):
            raise FaydaAuthError("Missing required configuration parameters", 500)

        self.redis = redis_client or RedisConfig().init_redis()
        self.host_manager = HostConfigManager(host_configs)
        self.handler = FaydaOAuthHandler(self.redis, self.client_id, self.authorize_url, self.token_url, self.user_info_url, self.private_key, self.client_assertion_type)

    def authorize(self, origin: str, referer: str = "") -> Dict[str, str]:
        """Generate an authorization URL and session data."""
        return self.handler.authorize(self.host_manager, origin, referer)

    def authenticate(self, session_id: str, auth_code: str, csrf_token: str) -> Dict[str, Any]:
        """Authenticate a user with the provided auth code and session data."""
        return self.handler.authenticate(session_id, auth_code, csrf_token)

    def add_host(self, origin: str, redirect_uri: str) -> None:
        """Add a new host configuration."""
        self.host_manager.add_host(origin, redirect_uri)

    def remove_host(self, origin: str) -> None:
        """Remove a host configuration."""
        self.host_manager.remove_host(origin)
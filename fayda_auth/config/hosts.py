from typing import Dict, List, Union
from dataclasses import dataclass

@dataclass
class HostConfig:
    origin: str
    redirect_uri: str

class HostConfigManager:
    def __init__(self, host_configs: Union[Dict[str, str], List[HostConfig]]):
        """
        Initialize the HostConfigManager with user-provided host configurations.

        :param host_configs: Required host configurations as a dict or list of HostConfig.
        """
        self.host_map: Dict[str, str] = {}

        if not host_configs:
            raise ValueError("host_configs must be provided and cannot be empty")

        self.load_from_input(host_configs)

        if not self.host_map:
            raise ValueError("No valid host configurations provided")

    def load_from_input(self, host_configs: Union[Dict[str, str], List[HostConfig]]) -> None:
        """Load host configurations from the provided input."""
        if isinstance(host_configs, dict):
            for origin, redirect_uri in host_configs.items():
                if not origin or not redirect_uri:
                    continue
                self.host_map[origin] = redirect_uri
        elif isinstance(host_configs, list):
            for config in host_configs:
                if not config.origin or not config.redirect_uri:
                    continue
                self.host_map[config.origin] = config.redirect_uri
        else:
            raise ValueError("host_configs must be a dict or list of HostConfig")

    def get_redirect_uri(self, origin: str) -> str:
        """Get the redirect URI for a given origin."""
        return self.host_map.get(origin)

    def add_host(self, origin: str, redirect_uri: str) -> None:
        """Add a new host configuration dynamically."""
        if not origin or not redirect_uri:
            raise ValueError("Both origin and redirect_uri must be non-empty")
        self.host_map[origin] = redirect_uri

    def remove_host(self, origin: str) -> None:
        """Remove a host configuration."""
        self.host_map.pop(origin, None)
import requests
from typing import Dict, Any, Optional
import logging
from requests.exceptions import RequestException
import time

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 30
    ) -> requests.Response:
        """
        Make HTTP request with proper error handling and logging
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            self.logger.info(f"Making {method} request to {url}")
            start_time = time.time()
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=headers,
                timeout=timeout
            )
            response_time = time.time() - start_time
            response.elapsed_time = response_time
            self.logger.info(f"Request completed in {response_time:.2f} seconds")
            response.raise_for_status()
            return response
        except RequestException as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise

    def check_response_time(self, response: requests.Response, max_time: float) -> bool:
        """
        Check if response time is within acceptable limits
        """
        return response.elapsed_time <= max_time

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        return self._make_request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        return self._make_request("POST", endpoint, json=json, **kwargs)

    def put(self, endpoint: str, json: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        return self._make_request("PUT", endpoint, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._make_request("DELETE", endpoint, **kwargs) 
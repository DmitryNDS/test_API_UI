import requests
from typing import Dict, Any, Optional
from jsonschema import validate
import json

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json_schema: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        """
        Make an HTTP request and validate response against JSON schema if provided.
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(
            method=method,
            url=url,
            json=data,
            params=params,
            headers=headers
        )
        
        if json_schema:
            validate(instance=response.json(), schema=json_schema)
            
        return response

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json_schema: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        return self._make_request("GET", endpoint, params=params, headers=headers, json_schema=json_schema)

    def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json_schema: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        return self._make_request("POST", endpoint, data=data, headers=headers, json_schema=json_schema)

    def put(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json_schema: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        return self._make_request("PUT", endpoint, data=data, headers=headers, json_schema=json_schema)

    def delete(
        self,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        json_schema: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        return self._make_request("DELETE", endpoint, headers=headers, json_schema=json_schema) 
import requests
from typing import Dict, Union, Optional
from rootshell_platform_api.config import API_ENDPOINT, BEARER_TOKEN
from http import HTTPStatus
import json

class BaseAPIClient:
    def __init__(self, base_url: str, headers: Optional[Dict] = None):
        self.base_url = f"{base_url}"
        self.headers = headers or {
            "Authorization": f"Bearer {BEARER_TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
    ) -> Union[Dict, str]:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method, url, headers=self.headers, params=params, json=data
            )
            if response.status_code == HTTPStatus.CREATED:
                return response.json()
            elif response.status_code == HTTPStatus.OK:
                if '<!doctype html>' in response.text.lower():
                    raise SystemExit({"error": "BEARER or API_ENDPOINT are incorrect"})
                return response.json()
            elif response.status_code == HTTPStatus.NO_CONTENT:
                return {"success": "No Content to display"}
            elif response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
                print(response.content)
                return {"error": json.loads(response.content)["message"]}
            elif response.status_code == HTTPStatus.UNAUTHORIZED:
                raise SystemExit({"error": json.loads(response.content)["message"]})
            elif response.status_code == HTTPStatus.FORBIDDEN:
                raise SystemExit({"error": json.loads(response.content)["message"]})
            elif response.status_code == HTTPStatus.BAD_REQUEST:
                raise SystemExit({"error": json.loads(response.content)["message"]})
            elif response.status_code == HTTPStatus.NOT_FOUND:
                raise SystemExit({"error": json.loads(response.content)["message"]})
            elif response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
                raise SystemExit({"error": json.loads(response.content)["message"]})
            elif response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
                raise SystemExit({"error": json.loads(response.content)["message"]})
            else:
                raise response.raise_for_status()

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": str(err)}

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Union[Dict, str]:
        return self._make_request("GET", endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict] = None) -> Union[Dict, str]:
        return self._make_request("POST", endpoint, data=data)

    def put(self, endpoint: str, data: Optional[Dict] = None) -> Union[Dict, str]:
        return self._make_request("PUT", endpoint, data=data)

    def delete(self, endpoint: str, data: Optional[Dict] = None) -> Union[Dict, str]:
        return self._make_request("DELETE", endpoint, data=data)

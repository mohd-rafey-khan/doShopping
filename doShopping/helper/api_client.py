import requests
from . import responses
from .messages import success_message_data,error_message_data


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            return responses.Response.bad_request(message = error_message_data['TOKEN_NOT_FOUND'])


    def post(self, endpoint, data=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            return responses.Response.bad_request(message = error_message_data['TOKEN_NOT_FOUND'])


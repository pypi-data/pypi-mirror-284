import requests
from .base import Base

class Auth(Base):
    def __init__(self, url: str):
        super().__init__(url)

    def sign_up(self, params: dict) -> str:
        response = requests.post(f'{self.url}/sign-up', json=params, headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        self.set_token(payload)
        return payload

    def sign_in(self, params: dict) -> str:
        response = requests.post(f'{self.url}/sign-in', json=params, headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        self.set_token(payload)
        return payload

    def verify_phone(self, params: dict) -> str:
        response = requests.post(f'{self.url}/verify-phone', json=params, headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        return payload

    def verify_email(self, params: dict) -> str:
        response = requests.post(f'{self.url}/verify-email', json=params, headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        return payload

    def check_username(self, username: str) -> bool:
        response = requests.post(f'{self.url}/check-username', json={'username': username}, headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        return bool(payload)

    def check_phone(self, phone: str) -> bool:
        response = requests.post(f'{self.url}/check-phone', json={'phone': phone}, headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        return bool(payload)

    def check_mail(self, mail: str) -> bool:
        response = requests.post(f'{self.url}/check-mail', json={'mail': mail}, headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        return bool(payload)

    def active_account(self, params: dict) -> str:
        response = requests.post(f'{self.url}/active-account', json=params, headers=self.headers)
        payload = response.text
        if not response.ok:
            raise Exception(payload)
        return payload
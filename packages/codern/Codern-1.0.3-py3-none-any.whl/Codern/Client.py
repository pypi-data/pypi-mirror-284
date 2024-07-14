import requests
import json
from typing import Literal

class Email:
    def __init__(
            self,
            To: str,
            text: str | int,
            Title: str,
            Token: str,
            Input: Literal['info', 'app', 'Login', 'support'] = 'info'
        ) -> None:
        self.To = To
        self.text = text
        self.Title = Title
        self.Input = Input
        self.Token = Token
    
    def Send(self):
        Data = {
            'email': self.To,
            'text': str(self.text),  # تبدیل به رشته اطمینان می‌دهد که همیشه رشته است
            'head': self.Title,
            'token': self.Token,
            'title': self.Input
        }
        
        url = 'https://api-free.ir/api2/email.php'
        response = requests.post(url, data=Data)
        pars = response.json()
        print(pars)
        
        if pars.get('ok', False):
            return {
                'state': 'ok',
                'code': 200
            }
        else:
            return False

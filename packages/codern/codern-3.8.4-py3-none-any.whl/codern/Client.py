try:
    import requests,urllib3,os
    from colorama import init, Fore, Style
except:
    import os
    os.system("pip install colorama && requests && urllib3")
import json
from typing import Literal

class Email:
    def __init__(
            self,
            To: str,
            text: str,
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

class api():
    def __init__(self,token,welcom: None = True)-> None:
        self.token=token
        self.welcom=welcom
        if welcom:
            message = f"""\n
            {Style.BRIGHT}Welcome to our library codern 3.8.16 !
            {Fore.GREEN}Website Dev : {Fore.RED}api-free.ir"""
            print(message)
    def Upload_file(byte_file:bytes,self:None):
        req=requests.post(
            "https://api-free.ir/api2/upload.php",
            data={'token':self.token},
            files={"file":byte_file},
            timeout=60
        ).json()['result']
        return req
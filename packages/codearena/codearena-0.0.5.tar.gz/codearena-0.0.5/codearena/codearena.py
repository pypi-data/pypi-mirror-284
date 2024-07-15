# coding: utf-8

# CodeArena Python SDK
# Author: Mingzhe Du (mingzhe@nus.edu.sg / mingzhe001@ntu.edu.sg)
# Date: 14 / 07 / 2024

import requests
from typing import Dict, List

class CodeArena(object):
    def __init__(self, url_root: str, token: str) -> None:
        self.token = token
        self.url_root = url_root
        
    def authenticate(self, token:str) -> bool:
        # TODO: token validation 
        self.token = token
        return True
    
    def get_problems(self, params={}) -> List:
        url = f"{self.url_root}/api/v2/problems"
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.request("GET", url, params=params, headers=headers)
        return response.json()
    
    def get_problem(self, problem_id: str) -> Dict:
        url = f"{self.url_root}/api/v2/problem/{problem_id}"
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.request("GET", url, headers=headers)
        return response.json()
    
    def get_submissions(self, params={}) -> List:
        url = f"{self.url_root}/api/v2/submissions"
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.request("GET", url, params=params, headers=headers)
        return response.json()
    
    def get_submission(self, submission_id: int) -> Dict:
        url = f"{self.url_root}/api/v2/submission/{str(submission_id)}"
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.request("GET", url, headers=headers)
        return response.json()
    
    def post_submission(self, problem_id: str, language: str, source: str) -> Dict:
        url = f"{self.url_root}/api/v2/submission"
        payload = {'problem_code': problem_id, 'language': language, 'source': source}
        headers = {'Authorization': f'Bearer {self.token}',}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

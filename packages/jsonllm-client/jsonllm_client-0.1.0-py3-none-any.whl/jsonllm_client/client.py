from typing import Optional, List, Dict, Union

import requests

from pathlib import Path


class JsonLLM:

    def __init__(self, api_key: str, url: str = "https://jsonllm.com"):
        self.api_key = api_key
        self.url = url

    def extract(
            self,
            project: Optional[str] = None,
            model: Optional[str] = None,
            filename: Optional[str] = None,
            filenames: Optional[str] = None,
            subset: Optional[List[str]] = None,
            texts: Optional[List[str]] = None,
    ) -> Dict:
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        body = {
            "project": project,
            "model": model,
            "filename": filename,
            "filenames": filenames,
            "subset": subset,
            "texts": texts,
        }
        response = requests.post(f"{self.url}/api/extract/", headers=headers, json=body)
        self._raise_error_if_bad_status_code(response)
        return response.json()

    def upload(self, project: str, paths: List[Union[str, Path]]):
        if isinstance(paths, str):
            paths = [Path(paths)]
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        files = {}
        for path in paths:
            path = Path(path)
            files[path.name] = path.read_bytes()
        data = {
            'project': project
        }
        response = requests.post(f"{self.url}/api/document/", files=files, headers=headers, data=data)
        self._raise_error_if_bad_status_code(response)
        return response.json()

    def add_text(self, project: str, filename: str, text: str):
        if not filename.endswith(".txt"):
            filename += ".txt"
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        files = {
            filename: text.encode('utf-8')
        }
        data = {
            'project': project
        }
        response = requests.post(f"{self.url}/api/document/", files=files, headers=headers, data=data)
        self._raise_error_if_bad_status_code(response)
        return response.json()


    def delete_documents(self, project: str, filename: str):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            "project": project,
            "filename": filename
        }
        response = requests.delete(f"{self.url}/api/document/", headers=headers, json=data)
        self._raise_error_if_bad_status_code(response)
        return response.json()


    def _raise_error_if_bad_status_code(self, response):
        if 400 <= response.status_code < 500:
            raise ValueError(response.text)
        elif 500 <= response.status_code < 600:
            raise ValueError(response.text)



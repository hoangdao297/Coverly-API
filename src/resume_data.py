import requests
from dotenv import dotenv_values

class GetResumeData:

    def __init__(self,resumelink) -> None:
        self.resumelink=resumelink
        secrets=dotenv_values('api_keys.env')
        self.__apikey=secrets['resume_reader_key']
        url = "https://api.affinda.com/v2/resumes"
        headers = {
            "accept": "application/json",
            "content-type": "multipart/form-data; boundary=---011000010111000001101001",
            "authorization": "Bearer "+self.__apikey
        }
        payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"wait\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"url\"\r\n\r\n"+resumelink+"\r\n-----011000010111000001101001--\r\n\r\n"
        response = requests.post(url, data=payload, headers=headers)
        self.__data=response.json()

    def getdata(self):
        return self.__data['data']

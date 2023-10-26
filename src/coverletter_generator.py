from dotenv import dotenv_values
from hugchat import hugchat
from hugchat.login import Login
from resume_prompt import ResumePrompt

class CoverLetter:
    
    def __init__(self) -> None:
        secrets=dotenv_values('h.env')
        self.__email=secrets['EMAIL']
        self.__passwd=secrets['PASSWD']

    def generateResult(self, prompt):
        sign = Login(self.__email, self.__passwd)
        cookies = sign.login()
        chatbot=hugchat.ChatBot(cookies=cookies.get_dict())
        answer=chatbot.chat(prompt)
        return answer[answer.index("Dear"):]

    def createPrompt(self, resumelink, joblink, personalities, relatedhobbies, awards): 
        resume=ResumePrompt(resumelink)
        name=resume.nameprompt()
        prevexperience="\nPrevious Experience: "+resume.experienceprompt()
        skills="\nSkills: "+resume.skillprompt()
        prompt="Based on this job link: "+joblink+"\n and based on these information: "+prevexperience+skills
        if personalities!=None:
            prompt+="\nPersonalities: "+personalities
        if relatedhobbies!=None:
            prompt+="\nHobbies: "+relatedhobbies
        if awards!=None:
            prompt+="\nAwards: "+awards
        prompt+="\nGive me a cover letter with my name: "+name
        return prompt

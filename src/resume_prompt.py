from resume_data import GetResumeData

class ResumePrompt:
    
    def __init__(self, resumelink) -> None:
        self.__resume=GetResumeData(resumelink)

    def skillprompt(self)->str:
        data=self.__resume.getdata()
        skills_prompt="".join([skill["name"]+"\n" for skill in data["skills"]])
        return skills_prompt
    
    def educationprompt(self)->str:
        data=self.__resume.getdata()
        education_prompt="\n"+"".join(["School: "+education["organization"]+", graduation date: "+education["dates"]["completionDate"]+"\n" for education in data["education"]])
        return education_prompt
    
    def nameprompt(self)->str:
        data=self.__resume.getdata()
        name_prompt="\n"+data["name"]["raw"]
        return name_prompt
    
    def experienceprompt(self)->str:
        data=self.__resume.getdata()
        expr_prompt="\n"+"".join(["\nJob Title: "+expr["jobTitle"]+"\nCompany: "+expr["organization"]+"\nJob description: "+expr["jobDescription"]+"\n" for expr in data["workExperience"]])
        return expr_prompt
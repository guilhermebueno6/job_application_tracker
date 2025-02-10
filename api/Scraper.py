from bs4 import BeautifulSoup
import requests
import os
import openai
from dotenv import load_dotenv
import sqlite3
from api.JobApplication import JobApplication
import html2text
load_dotenv()

class Scraper:
    
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    JOB_DESCRIPTION_CLASS = "show-more-less-html__markup"
    JOB_TITLE_CLASS = "topcard__title"
    JOB_COMPANY_CLASS = "topcard__org-name-link"
    PARSER = "html.parser"
    CHAT_GPT_KEY = os.getenv('CHAT_GPT_TOKEN')
    CHAT_GPT_MODEL = "gpt-4o-mini"
    JSON_SCHEMA='{"name": "skills_schema","strict": true,"schema": {"type": "object","properties": {"skills": {"type": "array","description": "A list of skills the job application.","items": {"type": "string"}}},"required": ["skills"],"additionalProperties": false}}'

    

    def archiveJob(self, link: str):
        
        response = requests.get(link, self.HEADERS)

        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, self.PARSER)

            # json = {
            #     "link": link,
            #     "job_description": self.getJobDescription(soup=soup),
            #     "job_title": self.getJobTitle(soup=soup),
            #     "company_name": self.getCompanyName(soup=soup),
            #     }
            application = JobApplication()
            application.link = link
            application.description =  self.getJobDescription(soup)
            application.title =  self.getJobTitle(soup)
            application.company =  self.getCompanyName(soup)
            if(self.CHAT_GPT_KEY):
                application.skills = self.getRelevantSkills(application.description)
            application.saveApplication()
            

            

    def getJobDescription(self, soup: BeautifulSoup):
        h = html2text.HTML2Text()
        h.ignore_links = True
        html = soup.find(class_=self.JOB_DESCRIPTION_CLASS)
        return h.handle(f"""{html}""")

    
    def getCompanyName(self, soup: BeautifulSoup):
        return soup.find(class_=self.JOB_COMPANY_CLASS).text.strip()
    
    def getJobTitle(self, soup: BeautifulSoup):
        return soup.find(class_=self.JOB_TITLE_CLASS).text.strip()
    
    def getRelevantSkills(self, description: str):
        openai.api_key = self.CHAT_GPT_KEY

        completion = openai.chat.completions.create(
            model=self.CHAT_GPT_MODEL,
            messages=[
                {"role": "system", "content": "You will summarize the following job descriptions listing all the hard skills contained in the text as a json object with name skills"},
                {"role": "user", "content": description},
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "skills_schema",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                        "skills": {
                            "type": "array",
                            "description": "A list of skills the job application.",
                            "items": {
                            "type": "string"
                            }
                        }
                        },
                        "required": [
                        "skills"
                        ],
                        "additionalProperties": False
                    }
                }
            }
        )


        return completion.choices[0].message.content

        # return client.res
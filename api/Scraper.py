from bs4 import BeautifulSoup
import requests

class Scraper:

    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    JOB_DESCRIPTION_CLASS = "show-more-less-html__markup"
    JOB_TITLE_CLASS = "topcard__title"
    JOB_COMPANY_CLASS = "topcard__org-name-link"
    PARSER = "html.parser"

    def archiveJob(self, link: str):
        
        response = requests.get(link, self.HEADERS)

        if(response.status_code == 200):
            soup = BeautifulSoup(response.text, self.PARSER)
            json = {
                "link": link,
                "job_description": self.getJobDescription(soup=soup),
                "job_title": self.getJobTitle(soup=soup),
                "company_name": self.getCompanyName(soup=soup),
                }
            
            with open("data/applications.json", mode="w", encoding="utf-8") as fjson:
                fjson.append(json)
            

    def getJobDescription(self, soup: BeautifulSoup):
        return soup.find(class_=self.JOB_DESCRIPTION_CLASS).text.strip()
    
    def getCompanyName(self, soup: BeautifulSoup):
        return soup.find(class_=self.JOB_COMPANY_CLASS).text.strip()
    
    def getJobTitle(self, soup: BeautifulSoup):
        return soup.find(class_=self.JOB_TITLE_CLASS).text.strip()
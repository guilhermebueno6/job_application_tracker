import requests
from bs4 import BeautifulSoup

payload = { 'api_key': '50880a8e305e52fb1866c17e90018bd3', 'url': 'https://www.linkedin.com/jobs/view/4136914561/'}
url = "https://www.linkedin.com/jobs/view/4136914561/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    jobDescription = soup.find(class_="show-more-less-html__markup")
    companyTitle = soup.find(class_="topcard__org-name-link")
    jobTitle = soup.find(class_='topcard__title')
    if jobDescription:
        print(jobTitle.text.strip())
    else:

        print('couldnt find element')
        with open("output.html", "w", encoding='utf-8') as f:
            f.write(str(soup))
        print(soup)
    # html_content = response.text
    # print(html_content)  # Prints the raw HTML of the page
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
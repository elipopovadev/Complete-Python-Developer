import requests
import pprint
from bs4 import BeautifulSoup

res = requests.get('https://dev.bg/?s=python+data&post_type=job_listing')
soup = BeautifulSoup(res.content, 'html.parser')

jobs_items = soup.find_all(class_='job-list-item')
result = []

for job in jobs_items:
    title = job.find(
        class_='job-title ab-title-placeholder ab-cb-title-placeholder').text.strip()
    company = job.find(class_='inner-left company-logo-wrap')
    company_name = company.find(
        class_='company-name hide-for-small').text.strip()
    date = job.find(class_='date date-with-icon').text
    result.append(
        {'Job Title': title, 'Company Name': company_name, 'Date': date})

pprint.pprint(result)

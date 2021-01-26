from bs4 import BeautifulSoup
import requests

URL = 'https://www.indeed.com/jobs?q=software+engineer&l=White+Plains%2C+NY'
page = requests.get(URL)

parsedData = BeautifulSoup(page.content, 'html.parser')
results = parsedData.find(id='pageContent')
job_elems = results.find_all(class_='jobsearch-SerpJobCard')

for job_elem in job_elems:
    title_elem = job_elem.find(class_='title')
    company_elem = job_elem.find(class_='company')
    location_elem = job_elem.find(class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
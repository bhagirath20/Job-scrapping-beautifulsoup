import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# print(soup)  #same as request page.text output . print(page.text)

results = soup.find(id="ResultsContainer")
# print(results.prettify())

job_elements = results.find_all("div", class_="card-content")



# for job_element in job_elements:
#     print(job_element, end="\n"*2)

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element)
#     print(company_element)
#     print(location_element)
#     print()

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text)
#     print(company_element.text)
#     print(location_element.text)
#     print()

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()

# python_jobs = results.find_all("h2", string="Ship broker")
# print(python_jobs)
selectedjobs = []
search  = input("Search keyword job title = ")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    title = title_element.text.strip().lower()
    if search in title:
        onejob = []
        onejob.extend([title_element.text.strip(),company_element.text.strip(),location_element.text.strip()])
        selectedjobs.append(onejob)
        # selectedjobs = selectedjobs.extend(onejob)
        # print(title_element.text.strip())
        # print(company_element.text.strip())
        # print(location_element.text.strip())
        # print()

    
df1 = pd.DataFrame(selectedjobs)
print(df1)

print()
print(df1.describe())
print()
print("perfect!!!")
import requests
from bs4 import BeautifulSoup
import json
import time

def getCourses (url):

    response = requests.get("https://www.coursera.org"+url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <p> tag that contain Enrollment numbers
        SpecializationEnrollment = soup.find('strong').text  if  soup.find('strong') is not None else 'NONE'
   
        Specializationcourses = soup.find('div', id="courses")
        SpecializationcoursesList = Specializationcourses.find_all('div', attrs={'data-testid': 'accordion-item'})
        output = []
        for Specializationcourse in SpecializationcoursesList:
            CourseTitle = Specializationcourse.find('h3').text
            CourseLink =  Specializationcourse.find("a").get('href') 
            CourseInfo =  Specializationcourse.find('div' , class_="cds-119 css-mc13jp cds-121").text
            thisdict = {"CourseTitle":CourseTitle ,"CourseLink":CourseLink ,"CourseInfo":CourseInfo}
            output.append(thisdict)
        return output
        


      
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')


# Opening JSON file
with open('SpecializationsList.json', 'r') as f:
  data = json.load(f)


specializations_links = [d.get("SpecializationsLink") for d in data]


for index,specializations_link in enumerate(specializations_links , ):
    data[index]["courses"] = getCourses(specializations_link)
    print(index,specializations_link)



with open('SpecializationsCourcesList.json', 'w') as json_file:
    json.dump(data, json_file)
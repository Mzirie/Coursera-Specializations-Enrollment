import requests
from bs4 import BeautifulSoup
import json


def getCoursesenrollment(url):

    response = requests.get("https://www.coursera.org"+url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the <p> tag that contain Enrollment numbers
        SpecializationEnrollment = soup.find('strong').text  if  soup.find('strong') is not None else 'NONE'
        return SpecializationEnrollment
        
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

# Opening JSON file
with open('SpecializationsCourcesList.json', 'r') as f:
  data = json.load(f)



# CourseLinklist = [obj["CourseLink"] for entry in data for obj in entry["courses"]]

i =0
for entry in data:
    for course in entry["courses"]:
        # Extract enrolment data (you can replace this with actual enrolment data)
        enrolment_data = "Enrollment data here"  # Replace with your data

        # Add 'enrolment' key to 'CourseInfo'
        course["enrollment"] = getCoursesenrollment(course['CourseLink'])
        i= i +1 
        print(i)
        

with open('SpecializationsCourcesListEnrolment.json', 'w') as json_file:
    json.dump(data, json_file)
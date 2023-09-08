import requests
from bs4 import BeautifulSoup
import json
import time

def getPageNumbers(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the div element with class "pagination-controls-container"
        pagination_div = soup.find('div', class_='pagination-controls-container')

        # Find the last button element within the pagination div
        last_button = pagination_div.find_all('button')[-2]

        # Extract the page number from the last button's text
        page_number = last_button.text
        return page_number

def getSpecializations(url):

    response = requests.get("https://www.coursera.org/"+url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <ul> element with the specified class
        ul_element = soup.find('ul', class_='cds-9 css-18msmec cds-10')

        # Find all <li> elements within the <ul> element
        li_elements = ul_element.find_all('li')

        output = []
        # Loop through the <li> elements and print their text content
        for li in li_elements:
            partnerNames = li.find("p", class_="cds-119 cds-ProductCard-partnerNames css-dmxkm1 cds-121").text 
            SpecializationsLink = li.find("a").get('href') 
     
            SpecializationsTitle = li.find("h3").text
            print(SpecializationsTitle)
            description = li.find("p", class_="cds-119 css-dmxkm1 cds-121").text 
            Reviews = li.find("div", class_="product-reviews").text if  li.find("div", class_="product-reviews") is not None else 'NONE'
            meta = li.find("div", class_="cds-CommonCard-metadata").text 

            thisdict = { "partnerNames": partnerNames, "SpecializationsLink": SpecializationsLink,"SpecializationsTitle": SpecializationsTitle , "description":description , "Reviews":Reviews , "meta":meta}
            output.append(thisdict)
        return output
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

def getgetSpecializationsFromPages(numberofpages):
    out = []
    for i in range(int(numberofpages)+1):
       time.sleep(0.5)

       out.append(getSpecializations(f'https://www.coursera.org/search?productTypeDescription=Specializations&page={i}'))
       print(f'https://www.coursera.org/search?productTypeDescription=Specializations&page={i}')
    return out

getPageNumber = getPageNumbers('https://www.coursera.org/search?productTypeDescription=Specializations')

getgetSpecializationsFromPage = getgetSpecializationsFromPages(getPageNumber)

print(getgetSpecializationsFromPage)

flat_array = [element for sublist in getgetSpecializationsFromPage for element in sublist]

with open('SpecializationsList.json', 'w') as json_file:
    json.dump(flat_array, json_file)








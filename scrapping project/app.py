from bs4 import BeautifulSoup
import requests





def temperature():
    
    try:
        
        search = "my location"
        url1 = "https://www.google.com/search?query={search}"
        r1 = requests.get(url1)
        data1 = BeautifulSoup(r1.text, "html.parser")
        location = data1.find("div", class_="BNeawe").text
        search_temp = "temperature in " + location
        
        url2 = "https://www.google.com/search?query={search_temp}"
        r2 = requests.get(url2)
        data2 = BeautifulSoup(r2.text, "html.parser")
        temp = data2.find("div", class_="BNeawe").text
        print("current temperature of {location} is {temp}")
        
    except Exception as e:
        print("Sorry sir I am unable to find this.")

           
if __name__ =="__main__":
    temperature()
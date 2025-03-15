from bs4 import BeautifulSoup

class Weather:
    def __init__(self):
        self.details = []
    
    def parse(self, html_file):
        with open(html_file, "r") as file:
            self.html_content = file.read()
        soup = BeautifulSoup(self.html_content,"html.parser")
        all_days = soup.find("tbody")
        days = all_days.find_all('tr')
        for day in days:
            day_info = day.find_all('td')
            self.details.append({"Day":day_info[0].text,"Temperature":int(day_info[1].text[:-3]),"Condition":day_info[2].text})

    def display(self):
        print("Day, Temperature, Condition")
        for detail in self.details:
            print(detail["Day"], detail["Temperature"],"°C", detail["Condition"])
    
    def find_days(self, info):
        print(f"{info.capitalize()} days: ")
        for detail in self.details:
            if detail["Condition"].lower()==info.lower():
                print(detail["Day"], detail["Temperature"], detail["Condition"])

    def find_highest_lowest(self):
        sorted_details = sorted([detail for detail in self.details], key= lambda x: x["Temperature"])
        lowest = sorted_details[0]
        highest = sorted_details[-1]
        print("The day with the highest:", highest["Day"], highest["Temperature"], highest["Condition"])
        print("The day with the lowest:", lowest["Day"], lowest["Temperature"], lowest["Condition"])

    def calculate_average_temperature(self):
        total = 0
        total = sum([day["Temperature"] for day in self.details])
        print(f"Average temperature: {round(total/len(self.details), 1)}°C")
def main():
    weather = Weather()
    weather.parse('weather.html')
    weather.display()
    weather.calculate_average_temperature()
    weather.find_days("sunny")
    weather.find_highest_lowest()
if __name__=="__main__":
    main()
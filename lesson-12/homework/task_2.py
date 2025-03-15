import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

class Jobs:
    def __init__(self):
        self.job_data = []
        self.base_url = "https://realpython.github.io/fake-jobs/"
    
    # Scrape the website
    def scrape(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a",string=lambda text: text and "Apply" in text)

        # ---Iterate through each job link using for loop---
        for link in links:
            link_response = requests.get(link["href"])
            link_soup = BeautifulSoup(link_response.text, "html.parser")

            job_title = link_soup.find(attrs={"class": "title is-2"}).text
            company_name = link_soup.find(attrs={"class": "subtitle is-4 company"}).text
            location = link_soup.find(attrs={"id":"location"}).text
            job_description = link_soup.find(attrs={"class":"content"}).text
            application_link = link["href"]
            job_info = (
                job_title, 
                company_name,
                location[10:],
                job_description,
                application_link
            )
            
            if job_title not in [job[0] for job in self.job_data] and company_name not in [job[1] for job in self.job_data] and location not in [job[2] for job in self.job_data]:
                self.job_data.append(job_info)
        print("Job details are scraped successfully!")
    def save_into_database(self):
        with sqlite3.connect("jobs.db") as connection:
            cursor = connection.cursor()
            cursor.execute("Create Table If not Exists jobs(Job_Title text, Company_Name text, Location text, Job_Description text, Application_Link text)")
            query = f"Insert into jobs Values(?, ?, ?, ?, ?)"
            cursor.executemany(query, self.job_data)

            print("Job details are saved in the database!")
    
    def filter(self, filter_type: str):
        if filter_type.lower() != "location" and filter_type.lower() != "company name":
            raise Exception("Invalid filter option!")
        if filter_type.lower()=="company name": option="Company_Name"
        else: option="Location"
        with sqlite3.connect("jobs.db") as connection:
            cursor = connection.cursor()
            query = f"Select * From jobs Order By {option}"
            filtered_data = cursor.execute(query)
            filtered_data_list = [list(job) for job in filtered_data.fetchall()]
        
        with open("jobs.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Job Title", "Company Name", "Location", "Job Description", "Application Link"])
            writer.writerows(filtered_data_list)
        print("Filtered data saved into CSV file!")
    def upgrade_check(self):
        with sqlite3.connect("jobs.db") as connection:
            cursor = connection.cursor()
            database_jobs = cursor.execute("Select * From jobs").fetchall()
            for i in range(len(database_jobs)):
                if self.job_data[i]!=database_jobs[i]:
                    query = f"Upgrade jobs Set Company_Name='{self.job_data[i][1]}', Location='{self.job_data[i][2]}', Job_Description='{self.job_data[i][3]}', Application_Link='{self.job_data[i][4]}'"
                    print(f"Information about the job has been updated: {self.job_data[i][0]}")
            else: print("Database is up-to-date!")
jobs = Jobs()
jobs.scrape()
jobs.save_into_database()
jobs.filter("company name")
jobs.upgrade_check()
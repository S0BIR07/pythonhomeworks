import csv
def read_subjects(filename: str):
    list_of_averages = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)   #Skip the header
        rows = list(reader)
        subjects = [row[1] for row in rows]
        unique_subjects = set(subjects)
        for subject in unique_subjects:
            grades = [int(row[2]) for row in rows if row[1]==subject]
            total=sum(grades)
            list_of_averages.append([subject, total/len(grades)])
    return list_of_averages
def write_records():
    with open("average_grades.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        writer.writerows(read_subjects("grades.csv"))

def main():
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([
            ['Name','Subject','Grade'],
            ['Alice','Math','85'],
            ['Bob','Science','78'],      # Example input for testing
            ['Carol','Math','92'],
            ['Dave','History','74']
        ])
    write_records()
if (__name__=="__main__"):
    main()
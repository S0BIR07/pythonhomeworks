universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(universities):
    enrollment_values = []
    tuition_fees = []
    for univers in universities:
        enrollment_values.append(univers[1])
        tuition_fees.append(univers[2])
    return enrollment_values, tuition_fees
def mean(lst):
    total = 0
    for val in lst:
        total+=val
    mean = round(float(total/len(lst)), 2)
    return mean
def median(lst):
    copy = sorted(lst)
    if len(copy)%2==0:
        median = (copy[int(len(copy)/2-1)]+copy[int(len(copy)/2)])/2
    else:
        median = copy[int((len(copy)-1)/2)]
    return median
enrollment_values = enrollment_stats(universities)[0]
tuition_fees = enrollment_stats(universities)[1]
student_mean = mean(enrollment_values)
student_median = median(enrollment_values)
tuition_mean = mean(tuition_fees)
tuition_median = median(tuition_fees)
total_students = int(sum(enrollment_values))
total_tuition = int(sum(tuition_fees))
print("*"*30)
print(f"Total students: {total_students}")
print(f"Total tuition: $ {total_tuition}\n")
print(f"Student mean: {student_mean}")
print(f"Student median: {student_median}\n")
print(f"Tuition mean: $ {tuition_mean}")
print(f"Tuition median: $ {tuition_median}")
print("*"*30)
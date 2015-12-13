import pdb

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for g in grades:
        print g

def grades_sum(grades):
    total = 0
    for g in grades:
        total += g
    return total

def grades_average(grades):
    return grades_sum(grades)/float(len(grades))

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance/float(len(scores))

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
total = 0

def print_grades(grades):
    for g in grades:
        print g

def grades_sum(grades):
    global total
    for g in grades:
        total += g

grades_sum(grades)
print total

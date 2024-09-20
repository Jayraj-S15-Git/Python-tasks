# functionss with para with return


#ex.1


'''def percentage():

    marks = [89,85,91,94,95,97]
    count = len(marks)
    total = 0
    for mark in marks:
        total += mark
    print(f"Total obtained Marks: {total}")
    print(f"Percentage: {round(total/count,2)}")
percentage()'''
'''
#ex.1
def percentage():
    marks = [89,85,91,94,95,97]
    print(f"Percentage: {round(sum(marks)/len(marks),2)}")
percentage()
'''


#ex.2

'''
def Percentage():
    raj = {
        "Maths":89,
        "Science":85,
        "English":91,
        "History":94,
        "Geography":95,
        "Marathi":97,
    }
    total = 0
    for subject in raj:
        print(subject+":"+str(raj[subject]))
        total += raj[subject]
    print(f"raj Have total {total} marks")
    print(f"raj Have {round(total/len(raj),2)}%")
Percentage()

'''


#ex.3
'''
def Percentage(student,name):
    total = 0
    for subject in student:
        print(subject+":"+str(student[subject]))
        total += student[subject]
    print(f"{name} Have total {total} marks")
    return round(total/len(student),2)
name = input("Enter Student Name: ")
student = {
    "Maths": int(input("Enter marks of Maths: ")),
    "Science": int(input("Enter marks of Science: ")),
    "English": int(input("Enter marks of English: ")),
    "H": int(input("Enter marks of Maths: ")),
    "Maths": int(input("Enter marks of Maths: ")),
    
Percentage()
    
'''
import pyhtml as h
from jinja2 import Template
import matplotlib.pyplot as plt
import csv
import sys

#Creates an html "output.html" with an error message.
def error_message():
    out = h.html(h.head(h.title("Something Went Wrong")), h.body(h.h1("Wrong Inputs"), h.p("Something went wrong")))
    temp = open('output.html', 'w')
    temp.write(out.render())
    temp.close()
    return 0


#Validationg input format.
try:
    if len(sys.argv) == 3:
        #print("argv len: ", len(sys.argv))
        if sys.argv[1] == '-s':
            if len(sys.argv[2]) == 4 and sys.argv[2][0] == '1' and int(sys.argv[2]) > 1000:
                given = "-s"
                #print("S_ID: ",int(sys.argv[2]))
            else:
                error_message()
                sys.exit()
        elif sys.argv[1] == '-c':
            if len(sys.argv[2]) == 4 and sys.argv[2][0] == '2'and int(sys.argv[2]) > 2000:
                given = "-c"
            else:
                error_message()
                sys.exit()
        else:
            error_message()
            sys.exit()
    else:
        error_message()
        sys.exit()
except:
    error_message()
    sys.exit()
#Reading the data.csv file.
file_temp1 = open("data.csv", 'r')
file = csv.DictReader(file_temp1)
total = 0
if given == "-s":
    dict_list = []
    for row in file:
        if row["Student id"] == sys.argv[2]:
            dict_list.append(row)
            total += int(row["Marks"])
else:
    course_marks_sum = 0
    course_count = 0
    course_marks_max = -1
    course_marks_list = []
    for row in file:
        if row["Course id"] == sys.argv[2]:
            converted_marks = int(row["Marks"]) 
            course_marks_list.append(converted_marks)
            course_marks_sum += converted_marks
            course_count += 1
            if converted_marks > course_marks_max:
                course_marks_max = converted_marks
    try:
        average = round(course_marks_sum/course_count, 2)
        plt.hist(course_marks_list)
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.savefig("histogram.png")
    except ZeroDivisionError:
        print("Given course doesn't match with any courses in the database.")
        sys.exit()

file_temp1.close()
#print(dict_list)
given_student = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>
                Student Data
            </title>
            <style>
                table, th, td{
                    border: 1px solid black;
                }
            </style>
        </head>
        <body>
            <h1>
                Student Details
            </h1>
            <table>
                <thead>
                    <tr>
                        <th>Student id</th>
                        <th>Course id</th>
                        <th>Marks</th>
                    </tr>
                </thead>
                <tbody>
                {% for i in dict_list %}
                    <tr>
                        <td>{{ i['Student id'] }}</td>
                        <td>{{ i['Course id'] }}</td>
                        <td>{{ i['Marks'] }}</td>
                    </tr>
                {% endfor %}
                </tbody>
                    <tr>
                        <td colspan="2"> Total Marks </td>
                        <td> {{total}} </td>
                    </tr>
            </table>
        </body>
    </html>
"""
given_course = """
<!DOCTYPE html>
    <html>
        <head>
            <title>
                Course Data
            </title>
            <style>
                table, th, td{
                    border: 1px solid black;
                }
            </style>
        </head>
        <body>
            <h1>
                Course Details
            </h1>
            <table>
                <thead>
                    <tr>
                        <th>Average Marks</th>
                        <th>Maximum Marks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{{ average }}</td>
                        <td>{{ course_marks_max }}</td>
                    </tr>
                </tbody>
            </table>
            <img src = "histogram.png" alt="Histogram of Marks">
        </body>
    </html>

"""
if given == "-s":
    #print(Template(temp).render(dict_list=dict_list))
    output = open('output.html', 'w')
    output.write(Template(given_student).render(dict_list=dict_list, total=total))
    output.close()
else:
    output = open('output.html', 'w')
    output.write(Template(given_course).render(average=average, course_marks_max=course_marks_max))
    output.close()




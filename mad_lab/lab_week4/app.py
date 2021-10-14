from flask import Flask
from flask import render_template
from flask import *
import csv
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


app = Flask(__name__)

file_temp1 = open("data.csv", 'r')
file = csv.DictReader(file_temp1)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST" and request.form["ID"] == "student_id":
        student_id = request.form["id_value"]
        file_temp1 = open("data.csv", 'r')
        file = csv.DictReader(file_temp1)
        total = 0
        dict_list = []
        for row in file:
            if row["Student id"] == student_id:
                dict_list.append(row)
                total += int(row[" Marks"])
        file_temp1.close()
        return render_template("student_details.html", dict_list=dict_list, total=total, student_id=student_id)
    elif request.method == "POST" and request.form["ID"] == "course_id":
        course_id = request.form["id_value"]
        file_temp1 = open("data.csv", 'r')
        file = csv.DictReader(file_temp1)
        course_marks_sum = 0
        course_count = 0
        course_marks_max = -1
        course_marks_list = []
        for row in file:
            if row[" Course id"] == course_id:
                converted_marks = int(row[" Marks"]) 
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
            return render_template("error.html")
        file_temp1.close()
        return render_template("course_details.html", average=average, course_marks_max=course_marks_max)
    else:
        return render_template("error.html")


if __name__ == '__main__':
    app.debug=True
    app.run()
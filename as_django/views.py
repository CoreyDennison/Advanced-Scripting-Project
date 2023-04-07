from django.http import HttpResponse
from as_django.models import students, attendance

# Create your views here.
def student_attend_view(request):
    student_obj = students.objects.get(student_id=3)
    student_fn = student_obj.first_name
    student_ln = student_obj.last_name
    student_num = student_obj.student_number
    student_course = student_obj.course

    student_attendance = attendance.objects.get(attendance_id=1)
    attendance_date = student_attendance.class_date
    s1_present = student_attendance.student1_present
    s2_present = student_attendance.student2_present
    s3_present = student_attendance.student3_present
    s4_present = student_attendance.student4_present
    s5_present = student_attendance.student5_present

    HTML = f"""
    
    <h2>Student Attendance App</h2>
    <h3>Students</h3>
    <table>
        <tr>
            <th>First Name</th>
            <th style = "border: 5px solid white;">Last Name</th>
            <th style = "border: 5px solid white;">Student Number</th>
            <th style = "border: 5px solid white;">Course</th>
        </tr>
        <tr>
            <td style = "border: 5px solid white;">{student_fn}</td>
            <td style = "border: 5px solid white;">{student_ln}</td>
            <td style = "border: 5px solid white;">{student_num}</td>
            <td style = "border: 5px solid white;">{student_course}</td>
        </tr>
    </table>
    
    <br>
    
    <h3>Attendance</h3>
    <table>
    <tr>
        <th>Class Date</th>
        <th style = "border: 5px solid white;">Student 1 Present</th>
        <th style = "border: 5px solid white;">Student 2 Present</th>
        <th style = "border: 5px solid white;">Student 3 Present</th>
        <th style = "border: 5px solid white;">Student 4 Present</th>
        <th style = "border: 5px solid white;">Student 5 Present</th>
    </tr>
    <tr>
        <td style = "border: 5px solid white;">{attendance_date}</td>
        <td style = "border: 5px solid white;">{s1_present}</td>
        <td style = "border: 5px solid white;">{s2_present}</td>
        <td style = "border: 5px solid white;">{s3_present}</td>
        <td style = "border: 5px solid white;">{s4_present}</td>
        <td style = "border: 5px solid white;">{s5_present}</td>
    </tr>
</table>
    """
    return HttpResponse(HTML)
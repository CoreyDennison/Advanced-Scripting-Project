from django.http import HttpResponse
# imports student and attendance models
from as_django.models import students, attendance
# imports loader from template module
from django.template import loader

def index_view(request):
    # Retrieves all values from each model.
    student_table = students.objects.all().values()
    attendance_table = attendance.objects.all().values()
    # context supplies the variables to display in the template in a Key:Value format
    context = {
        'students': student_table,
        'attendance': attendance_table,
    }

    # Locates the template index.html and loads it.
    template = loader.get_template('as_project/index.html')
    # The POST method sends data to create or update a resource.
    if request.method == "POST":
        John_is_present = request.POST.get('John_is_present', 'off')
        Michael_is_present = request.POST.get('Michael_is_present', 'off')
        Beth_is_present = request.POST.get('Beth_is_present', 'off')
        Nick_is_present = request.POST.get('Nick_is_present', 'off')
        Mark_is_present = request.POST.get('Mark_is_present', 'off')

        attendance_entry = attendance(
            john_present = John_is_present,
            michael_present = Michael_is_present,
            beth_present = Beth_is_present,
            nick_present = Nick_is_present,
            mark_present = Mark_is_present
        )

        attendance_entry.save()

    return HttpResponse(template.render(context,request))
from django.http import HttpResponse
from as_django.models import students, attendance
from django.template import loader

# Create your views here.
def index_view(request):
    student_table = students.objects.all().values()
    attendance_table = attendance.objects.all().values()
    template = loader.get_template('as_project/index.html')
    context = {
        'students': student_table,
        'attendance': attendance_table,
    }

    if request.method == "POST":
        John_is_present = request.POST.get('John_is_present', 'n')
        Michael_is_present = request.POST.get('Michael_is_present', 'n')
        Beth_is_present = request.POST.get('Beth_is_present', 'n')
        Nick_is_present = request.POST.get('Nick_is_present', 'n')
        Mark_is_present = request.POST.get('Mark_is_present', 'n')

        attendance_entry = attendance(
            student1_present = John_is_present,
            student2_present = Michael_is_present,
            student3_present = Beth_is_present,
            student4_present = Nick_is_present,
            student5_present = Mark_is_present
        )
        attendance_entry.save()


    return HttpResponse(template.render(context,request))
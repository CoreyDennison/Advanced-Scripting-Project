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

    return HttpResponse(template.render(context,request))
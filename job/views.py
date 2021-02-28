from django.shortcuts import render
from .models import Work
# Create your views here.


def job_list_view(request):
# list all jobs
    list_jobs = Work.objects.all()
    context={
        "jobs":list_jobs
    }
    return render(request, 'job/job_list.html',context)



def job_detail_view(request ,id):
    # Show job details
    pass

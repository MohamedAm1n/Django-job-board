from django.shortcuts import render
from .models import Work
# Create your views here.


def job_list_view(request):
# list all jobs
    list_jobs = Work.objects.all()
    context={
        "jobs":list_jobs ,# data send to template with this name
    }
    return render(request, 'job/job_list.html',context)


def job_details_view(request ,id):
    # Show job details
    job_detail = Work.objects.get(id=id)
    context={"job_detail":job_detail}
    return render(request, 'job/job_details.html',context)    

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Work
from .form import ApplayForm
# Create your views here.


def job_list_view(request):
# list all jobs
    list_jobs = Work.objects.all()
    job_count= Work.objects.count()
    paginator = Paginator(list_jobs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        "jobs":page_obj,
        'job_count':job_count
    }
    return render(request, 'job/job_list.html',context)


def job_details_view(request ,slug):
    # Show job details
    job_detail = Work.objects.get(slug=slug)
    if request.method == 'POST' :
        form = ApplayForm(request.POST,request.FILES)
        print('test')
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.work=job_detail
            myForm.save()
    else:
        form =ApplayForm()
        
    context={
        "job_detail":job_detail,
        "form":form    
            }
    return render(request, 'job/job_details.html',context)    

from django.shortcuts import render
from .models import Job

"""
(tob_list) => Job Page
[
    job_id 1, ---- cliecked id=1 ---> fetch job_id = 1 and put it in job_deatil Page
    job_id 2,
    job_id 3,
    job_id 4,
    ...
    job_id n
]
"""


def job_list(request):
    context = {"jobs": Job.objects.all()}
    print(context)
    return render(request, "pages/job_list.html", context)


def job_detail(request, id):
    context = {"job": Job.objects.get(id=id)}
    print(context)
    return render(request, "pages/job_detail.html", context)

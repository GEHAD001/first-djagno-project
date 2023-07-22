from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job

"""
class  = table
attribute = column
object = row
[
    object1, [row 1]
    object1, [row 2]
    object1, [row 3]
]
"""


def jobs(request):
    # call all row from database
    jobs = Job.objects.all()

    # sperate data on pages system
    paginator = Paginator(jobs, 6)

    # get the request page
    current_page_number = request.GET.get("page", 1)

    # return page object that contain the data
    page = paginator.get_page(current_page_number)

    page.adjusted_elided_pages = paginator.get_elided_page_range(
        current_page_number, on_each_side=1, on_ends=1
    )
    context = {
        "page": page,
        "number_of_jobs": jobs.count(),
    }
    return render(request, "job/jobs.html", context)


def job_detail(request, slug, id):
    print(id)
    print(slug)
    job = Job.objects.get(slug=slug, id=id)
    context = {"job": job}
    return render(request, "job/job_detail.html", context)

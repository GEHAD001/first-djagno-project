from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path("", views.jobs, name="jobs"),
    path("<str:slug>/id<int:id>", views.job_detail, name="job_detail"),
]

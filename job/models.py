from django.db import models


JOB_TYPE = (("Full Time", "Full Time"), ("Part Time", "Part Time"))


class Job(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=0)
    salary = models.FloatField(default=0.0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

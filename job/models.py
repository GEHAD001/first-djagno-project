from django.db import models

# Create your models here.


class mapping(models.Model):
    #   table       Column         Datatype
    title = models.CharField(max_length=25)


JOB_TYPE = (
    ("PT", "Part Time"),
    ("FT", "Full Time"),
)

# (Store as , Show as), Selected Part time and store in database PT


class job_1(models.Model):
    job_tilte = models.CharField(max_length=100)
    job_type = models.CharField(max_length=12, choices=JOB_TYPE)
    job_description = models.TextField(max_length=1200)
    published_at = models.DateTimeField(auto_now=True)
    exp = models.IntegerField(default=0)
    salary = models.FloatField(default=0.0)

    def __str__(self):
        return self.job_tilte

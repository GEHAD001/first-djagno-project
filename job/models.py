from django.db import models
from django.utils.text import slugify

JOB_TYPE = (("Full Time", "Full Time"), ("Part Time", "Part Time"))

# upload_to take function and pass image_row and image_name to the function


# How let the Image
def image_upload(row, image_name):
    # image_name => full image name with exetenstion
    # row => row that store image in
    image_name, exetention = image_name.split(".")

    # path that store image in + image name
    return f"jobs_images/{row.id}.{exetention}"


class Job(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=0)
    salary = models.FloatField(default=0.0)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=image_upload, default="")
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    slug = models.SlugField(null=True, blank=True)

    # override on save method in Model
    def save(self, *args, **kawrgs):
        # this line code added on the save method of the Model
        self.slug = slugify(self.title)

        # here call the same save method in Model
        super(Job, self).save(*args, **kawrgs)

    # object name in call
    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


"""
on_upload is a function that give:
    1. object from row that stored in
    2. file name [uploaded file]
and need:
    path + file.exetention [to Store]
    mean can control in path and file name
    
    Ex:
        dir/sub_dir/file.exe
"""

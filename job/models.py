from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
# 
JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Work(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.PositiveIntegerField(default=1)
    salary = models.PositiveIntegerField(default=0)
    experience = models.IntegerField(default=1)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return  self.title
# 
# # End of class Job






# # كنت بعمل الريليشن بين الوظيفة و الكاتيجوري
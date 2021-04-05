from django.db import models
from django.db.models.fields.files import FileField
from django.template.defaultfilters import slugify

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
def upload_image(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.published_at,extension)
pass
class Work(models.Model):
    title        = models.CharField(max_length=100)
    job_type     = models.CharField(max_length=15, choices=JOB_TYPE)
    description  = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy      = models.PositiveIntegerField(default=1)
    salary       = models.PositiveIntegerField(default=0)
    experience   = models.IntegerField(default=1)
    cat          = models.ForeignKey(Category,on_delete=models.CASCADE)
    image        = models.ImageField(upload_to=upload_image)
    slug         = models.SlugField(null=True , blank=True)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Work,self).save(*args, **kwargs)        
    def __str__(self):
        return self.title

class Apply(models.Model):
    work=models.ForeignKey(Work,related_name='apply_Work',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    webSite=models.URLField()
    cv=models.FileField(upload_to='Apply/')
    cover_letter=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
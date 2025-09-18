from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    profile = models.ForeignKey(Profile,related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    profile = models.ForeignKey(Profile,related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    
class Experience(models.Model):
    profile = models.ForeignKey(Profile,related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.company
    
class Education(models.Model):
    profile = models.ForeignKey(Profile,related_name='educations', on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.school
    
class Certification(models.Model):
    profile = models.ForeignKey(Profile,related_name='certifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Award(models.Model):
    profile = models.ForeignKey(Profile,related_name='awards', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return self.name
    

    
    
    
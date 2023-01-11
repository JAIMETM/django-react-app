from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=150)
    description= models.CharField(max_length= 200)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title



class Mission(models.Model):
    date_dep = models.DateField()
    date_dest = models.DateField()
    Ref_Rem = models.CharField (max_length=20)
    chauf_ref = models.CharField(max_length= 15)
    Ref_Track = models.CharField (max_length=20)
    status = models.CharField (max_length= 5, default=' ')

    def __str__(self):
        return self.Ref_Rem +  ""+ self.Ref_Track+" "+ self.chauf_ref

        


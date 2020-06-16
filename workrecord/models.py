from django.db import models

# Create your models here.
class WorkModel(models.Model):
    workingDate = models.DateField()
    workNumber = models.CharField(max_length=20)
    memo = models.TextField()
    workStartTime = models.DateTimeField()
    workEndTime = models.DateTimeField()
    
    def __str__(self):
        return '<Work : id=' + str(self.id) + ', ' + \
            str(self.workingDate) + '(' + self.workNumber + ') >'
from django.db import models
import datetime

# Create your models here.
class WorkModel(models.Model):
    workingDate = models.DateField(default=datetime.date.today)
    workNumber = models.CharField(max_length=20)
    memo = models.TextField()
    workStartTime = models.TimeField()
    workEndTime = models.TimeField()
    
    def __str__(self):
        return '<Work : id=' + str(self.id) + ', ' + \
            str(self.workingDate) + '(' + self.workNumber + ') >'
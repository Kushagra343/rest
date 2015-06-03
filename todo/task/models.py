from django.db import models

class Task(models.Model):
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return str(self.id)
    class Meta:
    	    db_table = 'Task'
    	    verbose_name = 'Task'
    	    verbose_name_plural = 'Tasks'
	

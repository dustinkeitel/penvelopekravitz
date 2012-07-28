from django.db import models

class Celebrity(models.Model):
    def __unicode__(self):
        return self.name
        
    name = models.CharField(max_length=300)
    flagged = models.BooleanField()
    whitelisted = models.BooleanField()
    #add_date = models.DateTimeField('date added')
    #contributor = models.ForeignKey('auth.User')

    class Meta:
        verbose_name_plural = 'celebrities'

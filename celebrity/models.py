from django.db import models
from django.forms import ModelForm

class Celebrity(models.Model):
    def __unicode__(self):
        return self.name
        
    name = models.CharField(max_length=300, help_text=None)
    flagged = models.BooleanField(default=False)
    whitelisted = models.BooleanField(default=False)
    #add_date = models.DateTimeField('date added')
    #contributor = models.ForeignKey('auth.User')

    class Meta:
        verbose_name_plural = 'celebrities'

class CelebrityForm(ModelForm):
    class Meta:
        model = Celebrity
        fields = ('name',)
        help_text = ""
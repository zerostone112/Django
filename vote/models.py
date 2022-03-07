from django.db import models
from acc.models import User

# Create your models here.
class Topic(models.Model):
    subject = models.CharField(max_length=200)
    maker = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    voter = models.ManyToManyField(User, blank=True, related_name="voter")
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.subject

    def summary(self):
        if len(self.content) > 15:
            return f"{self.content[:15]} ..."
        return self.content

class Choice(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    chname = models.CharField(max_length=200)
    chpic = models.ImageField(upload_to="vote/%y")
    chcom = models.TextField()
    choicer = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.topic}-{self.chname}"
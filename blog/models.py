from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def new_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')

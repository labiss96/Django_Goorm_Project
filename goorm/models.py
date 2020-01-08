from django.db import models
from accounts.models import Profile


class Brand(models.Model):
    brd_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brd_name

class Tobacco(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='tobacco')
    name = models.CharField(max_length=50)
    price = models.IntegerField(blank=True)
    rel_date = models.DateTimeField(blank=True)
    nicotine =  models.FloatField()
    TAR = models.FloatField()
    feel_of_hit = models.CharField(max_length=10)
    score = models.FloatField(default=0)
    #total_like = models.PositiveIntegerField(default=0)
    #like_user = models.ManyToManyField()
    isMenthol = models.BooleanField(default = False)
    img = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Comment(models.Model) :
    tobacco = models.ForeignKey(Tobacco, on_delete = models.CASCADE, related_name= 'comments')
    writer = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name= 'writer')
    pub_date = models.DateTimeField(auto_now_add= True)
    contents = models.TextField()
    score = models.PositiveIntegerField(default=3)
    


    def __str__(self) :
        return self.writer + "의 댓글"

# Create your models here.

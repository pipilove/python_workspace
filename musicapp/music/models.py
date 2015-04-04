from django.db import models

# Create your models here.
class Login(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length= 30,unique=True)
    passwd = models.CharField(max_length= 20)
    email = models.EmailField()
    def __unicode__(self):
        return self.user_name

# class User(models.Model):
#     user_id = models.ForeignKey(Login)
#     # gender = models.CharField(max_length=6,choices=(('f','female'),('m','male'),))
#     age = models.IntegerField(default=0)
#     country = models.CharField(max_length=50)
#     def __unicode__(self):
#         return self.user_id

class Item1(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length= 50)
    art_name = models.CharField(max_length= 30)
    item_link = models.URLField(null=True)
    def __unicode__(self):
        return self.item_name

class User(models.Model):
    user_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)
    timestamp = models.DateTimeField(null=True)
    preference = models.IntegerField(default=1)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.user_id)

class Item2(models.Model):
    # item_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length= 50)
    def __unicode__(self):
        return self.item_name

class Item2Tag(models.Model):
    # item_id = models.ForeignKey(Item2,primary_key=True)
    item_id = models.IntegerField(default=0)
    item_tag = models.CharField(max_length= 50)
    def __unicode__(self):
        return self.item_id

class Image(models.Model):
    img = models.ImageField()

class Hotmusic(models.Model):
    item_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length= 50,null=True)
    art_name = models.CharField(max_length= 30,null=True)
    item_link = models.URLField(null=True)
    def __unicode__(self):
        return self.item_name

class Recmusic(models.Model):
    user_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length= 50)
    art_name = models.CharField(max_length= 30,null=True)
    def __unicode__(self):
        return self.item_name
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Users(models.Model):
    '''
    this is a model class that defines how users will be created
    '''
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank= True)

class Profile(models.Model):
    photo = models.ImageField(upload_to='Image/')
    boi = models.CharField(max_length=300, blank = True),
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    #saving method
    def save_profile(self):
        """
        A method to save an object
        """
        self.save()

    #deleting method
    def delete_profile(cls, id):
        """
        A method to delete an object
        """
        return cls.objects.filter(id == id).delete()



class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', default = None)
    name = models.CharField(max_length=255)
    caption = models.TextField(max_length=255)
    # profiles = models.ForeignKey(Profile, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posted_by',blank= True)
    likes = models.ForeignKey(User, related_name='liked_by',on_delete=models.CASCADE, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
 

    


class Comment(models.Model):
    '''
    this is a blueprint that gives out a layout on how a comment will be made
    '''
    comment = HTMLField()
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE)
    posted_on = models.DateField(auto_now_add=True)
    image_id = models.ForeignKey(Image,on_delete= models.CASCADE)

    def add_comment(self):
        self.save()

    

    @classmethod
    def get_all_comments(cls):
        '''
        this is a classmethod that gets all comments from the db
        '''
        comments = cls.objects.all()
        return comments
    
class Like(models.Model):
    like = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_liked = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.like)
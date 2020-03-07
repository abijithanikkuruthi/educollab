from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    u_id = models.ForeignKey(User, related_name='member', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    institution = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=200)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.username

class Field(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Topic(models.Model):
    field = models.ForeignKey(Field, related_name='topic', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Subject(models.Model):
    topic = models.ForeignKey(Topic, related_name='subject', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Curriculum(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(Member, related_name='curriculum', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='curriculum', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified']

class Bit(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    bit_type = models.CharField(max_length=100)
    curriculum = models.ForeignKey(Curriculum, related_name='bit', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)    
    description = models.CharField(max_length=1000, default="")
    file = models.FileField(null=True, default=None)
    text = models.CharField(max_length=2000, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified']

class ChangeLog(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member, related_name='changelog', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    operation = models.CharField(max_length=100, null=True, default=None)
    curriculum = models.ForeignKey(Curriculum, related_name='changelog', on_delete=models.CASCADE, null=True, default=None)
    bit = models.ForeignKey(Bit, related_name='changelog', on_delete=models.CASCADE, null=True, default=None)
    subject = models.ForeignKey(Subject, related_name='changelog', on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.description


class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    member = models.ForeignKey(Member, related_name='comment', on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, related_name='comment', on_delete=models.CASCADE, null=True, blank=True)
    bit = models.ForeignKey(Bit, related_name='comment', on_delete=models.CASCADE, null=True, blank=True)
    changelog = models.ForeignKey(ChangeLog, related_name='comment', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment

class Upvote(models.Model):
    member = models.ForeignKey(Member, related_name='upvote', on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, related_name='upvote', on_delete=models.CASCADE, null=True) 
    bit = models.ForeignKey(Bit, related_name='upvote', on_delete=models.CASCADE, null=True)
    changelog = models.ForeignKey(ChangeLog, related_name='upvote', on_delete=models.CASCADE, null=True)

class Subscription(models.Model):
    member = models.ForeignKey(Member, related_name='subscription', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='subscription', on_delete=models.CASCADE, null=True)
    curriculum = models.ForeignKey(Curriculum, related_name='subscription', on_delete=models.CASCADE, null=True)

class Teach(models.Model):
    member = models.ForeignKey(Member, related_name='teach', on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, related_name='teach', on_delete=models.CASCADE)
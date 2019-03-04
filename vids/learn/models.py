from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vids(models.Model):
  name = models.CharField(max_length=50, unique = True,blank = True)
  description = models.CharField(max_length=100)
  video_file = models.CharField(max_length = 100, null= True)

  def __str__(self):
    return self.name

class VidTopics(models.Model):
  """
  A model to contain the various subject discussed in the video
  A video can have multiple Topic
  """
  subject = models.CharField(max_length = 255, unique = True)
  vids = models.ForeignKey(Vids,on_delete = models.CASCADE, related_name = 'topics')
  last_updated = models.DateTimeField(auto_now_add = True)
  starter = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'topics',null = True)

  def __str__(self):
    return self.subject

class ThreadDiscussion(models.Model):
  """
  A model to contain the various discussion threads
  """
  subject = models.ForeignKey(VidTopics, on_delete = models.CASCADE, related_name = 'subjetcs')
  thread_content = models.CharField(max_length =150)
  last_updated = models.DateTimeField(auto_now_add = True)
  discussed_by = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'subjects')

  def __str__(self):
    return self.thread_content


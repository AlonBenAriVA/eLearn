from django.shortcuts import render
from learn.models import Vids, VidTopics, ThreadDiscussion
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm, AddComment

# Create your views here.

def home (request):
  vids = Vids.objects.all()
  return render (request,'index.html',{'vids':vids})

def get_discussion(request, pk):
  vids = Vids.objects.get(pk=pk) # must have videos at a minimum
  print('pk:' ,pk)
  try:
    discussion = VidTopics.objects.filter(vids_id = pk)
  except:
    print('error')
    discussion = ''
  return render(request,'discussion.html',{'vids':vids, 'discussion': discussion,'pk':pk})

def get_thread(request,subject_id):
  """
  A view to return the relevant discussion thread
  """
  threads = [v for v in ThreadDiscussion.objects.filter(subject_id=subject_id)]
  print(threads)
  print(subject_id)
  return render(request, 'threads.html', {'threads':threads,'id':subject_id})

def new_topic(request,pk):
  """
  The view for the add new topic.
  """
  user = User.objects.first()
  if request.method == 'POST':
    form = NewTopicForm(request.POST)
    if form.is_valid():
      post = form.save(commit = False)
      post.subject = form.cleaned_data.get('subject'),
      post.vids = Vids.objects.get(pk=pk)
      post.starter = request.user
      post.save()
      ThreadDiscussion(
        subject = post,
        thread_content = form.cleaned_data.get('comment'),
        discussed_by = request.user
      ).save()
      return redirect('/learn/'+pk)
  else:
    form = NewTopicForm()
  return render(request,'new_topic.html',{'form':form,'videoName':Vids.objects.get(pk=pk).name})


def add_comment(request,subject_id):
  user = User.objects.first()
  if request.method == 'POST':
    form = AddComment(request.POST)
    if form.is_valid():
      post = form.save(commit = False)
      post.thread_content = form.cleaned_data.get('thread_content')
      print(post.thread_content)
      post.subject = VidTopics.objects.get(id = subject_id)
      post.discussed_by = request.user
      post.save()
      print('this worked')
    return redirect('/thread/'+subject_id)
  else:
    form = AddComment()
  return render(request, 'add_comment.html',{'form':form,'id':id})





  

  


  


#

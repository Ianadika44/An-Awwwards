from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import AwardLetterForm,NewPostForm
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email


# Create your views here.


def awards(request):
    projects = Post.objects.all()
    return render(request, 'awards.html')


@login_required(login_url='/accounts/login/')
def all_projects(request):
    award = Post.main()
    if request.method == 'POST':
        form = AwardLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = AwardLetterRecipients(name=name, email=email)
            recipient.save()
            HttpResponseRedirect('major')
    else:
        form = AwardLetterForm()
    return render(request, 'all-awards/major.html', {"award": award, "letterForm": form})

    return render(request, 'all-awards/main.html',)


def profile_info(request):

    current_user = request_user
    profile_user = Profile.objects.filter(user=current_user).first()
    projects = request.user.post.all()
    

    return render(request, 'all-awards/profile.html', {"projects": projects, "profile": profile_info, "current_user": current_user})


@login_required(login_url='/accounts/login/')
def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-awards/post.html", {"post": post})


def search_results(request):

    if 'posts' in request.GET and request.GET["posts"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-awards/search.html', {"message": message, "posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-awards/search.html', {"message": message})
    
    
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.User = current_user
            post.save
        return redirect('awards')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})
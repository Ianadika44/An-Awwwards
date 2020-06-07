from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import AwardLetterForm, NewPostForm
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from django.http import JsonResponse


# Create your views here.


def awards(request):
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
    return render(request, 'all-awards/main.html', {"awards": awards, "letterForm": form})

    return render(request, 'all-awards/major.html',)


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

    current_user = request.user
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


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    projects = Project.objects.filter(username=current_user)

    return render(request, 'profile.html', {"projects": projects, "profile": profile})


@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(username=user)
    projects = Project.objects.filter(username=user)



def single_project(request, c_id):
    current_user = request.user
    current_project = Post.objects.get(id=c_id)
    ratings = Rating.objects.filter(post_id=c_id)
    usability = Rating.objects.filter(
        post_id=c_id).aggregate(Avg('usability_rating'))
    content = Rating.objects.filter(
        post_id=c_id).aggregate(Avg('content_rating'))
    design = Rating.objects.filter(
        post_id=c_id).aggregate(Avg('design_rating'))

    return render(request, 'awards/project.html',
                  {"project": current_project, "user": current_user, 'ratings': ratings, "design": design,
                   "content": content, "usability": usability})


def review_rating(request, id):
    current_user = request.user

    current_project = Post.objects.get(id=id)

    if request.method == 'POST':
        form = ProjectRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = current_project
            rating.user = current_user
            rating.save()
            return redirect('project', id)
    else:
        form = ProjectRatingForm()

    return render(request, 'projects/rating.html', {'form': form, "project": current_project, "user": current_user})


def awardletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = AwardLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)
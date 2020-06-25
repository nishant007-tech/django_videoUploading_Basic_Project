from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Profile , Contact ,Playlist, Video
from django.contrib.auth import logout
from .forms import Profileupdateform
# Create your views here.


def index(request):
    v_play= Playlist.objects.order_by('-pubdate')
    return render(request, 'index.html', {'v_play':v_play})


def login(request):
    if request.method == 'POST':
        eml = request.POST['eml']
        pas = request.POST['pas']
        user = auth.authenticate(username=eml, password=pas)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        psw = request.POST['psw']
        psw2 = request.POST['psw-repeat']
        if psw == psw2:
            if User.objects.filter(username=email).exists():
                messages.info(request, "Email already taken!!")
            else:
                user = User.objects.create_user(
                    username=email, password=psw, first_name=name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not matching')
            return redirect('register')

    return render(request, 'register.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        cont = Contact(name=name, email=email, mobile=phone, msg=msg)
        cont.save()
        messages.success(request, 'Your Message has been sent!')
        return redirect('contact')
    return render(request, 'contact.html')


def logoutuser(request):
    logout(request)
    return redirect('index')

def profile(request):
    if request.method == 'POST':
        p_from = Profileupdateform(request.POST, request.FILES, instance=request.user.profile)  
        if p_from.is_valid():
            p_from.save()
            messages.success(request, 'Your profile has been successfully updated')
            return redirect('profile')

    else:
        p_form = Profileupdateform(instance=request.user.profile)

    context ={
        'p_form': p_form,
    }

    return render(request, 'profile.html', context)

def playlist(request):
    if request.method == 'POST':
        title = request.POST['title']
        desp = request.POST['mesg']
        play = Playlist(title=title, desp=desp)
        play.save()
        messages.success(request, 'Playlist has been created!')
        return redirect('index')
    return render(request, 'create_playlist.html')  


def see_playlist(request):
    v_video = Video.objects.order_by("-pubdate")
    return render(request, 'watch_playlist.html',{"v_video":v_video})


def upload_video(request):
    if request.method == 'POST':
        vtitle =request.POST['vtitle']
        vdesp =request.POST['vdesp']
        myfile =request.FILES['myfile']
        w_video = Video(title_of_video=vtitle, video_desp=vdesp, videofile=myfile)
        w_video.save()
        return redirect("see_playlist")
    return render(request, 'upload_video.html')

def remove_post(request,id):
    d_post= Video.objects.get(id=id)
    messages.success(request, 'You have successfully deleted your Video.')
    d_post.delete()
    return redirect('see_playlist')

def remove_playlist(request,id):
    d_play= Playlist.objects.get(id=id)
    messages.success(request, 'You have successfully deleted your Playlist.')
    d_play.delete()
    return redirect('index')
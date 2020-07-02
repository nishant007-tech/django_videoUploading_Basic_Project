from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Profile , Contact ,Playlist, Video, Demovideo
from django.contrib.auth import logout
from .forms import Profileupdateform, Videoform
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def index(request):
    demo_video = Demovideo.objects.order_by('-publishdate')
    v_play= Playlist.objects.order_by('-pubdates')
    return render(request, 'index.html', {
        'v_play':v_play,
        'demo_video':demo_video,
        })


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
        w_form = Videoform(request.POST, request.FILES)
        if w_form.is_valid():
            w_form.save()
            return redirect("see_playlist")
    else:
        w_form= w_form = Videoform(request.POST, request.FILES)
    return render(request, 'upload_video.html',{'w_form':w_form})

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


def c_password(request):
    if request.method == 'POST':
        c_form = PasswordChangeForm(request.user, request.POST)
        if c_form.is_valid():
            user = c_form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('c_password')
        else:
            messages.error(request, 'Something went wrong!!')
    else:
        c_form = PasswordChangeForm(request.user)
    return render(request, 'c_password.html', {'c_form':c_form})

def upload_demo(request):
    if request.method == 'POST':
        vttl =request.POST['vttl']
        vdsp =request.POST['vdsp']
        mfile =request.FILES['mfile']
        demo_video = Demovideo(title_demo=vttl, demo_desp=vdsp, videofiles=mfile)
        demo_video.save()
        return redirect("index")
    return render(request, 'video_demo.html')

def remove_demo(request,id):
    del_post= Demovideo.objects.get(id=id)
    messages.success(request, 'You have successfully deleted your Video.')
    del_post.delete()
    return redirect('index')

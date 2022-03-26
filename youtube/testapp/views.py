from django.shortcuts import render,redirect
from testapp.models import Info
from testapp.forms import Info_Form,Download_Form
# Create your views here.

def home_view(request):
    form=Info_Form()
    if request.method=='POST':
        form=Info_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/download')
    return render(request,'testapp/home.html',{'form':form})

from pytube import YouTube
def download_view(request):
    form=Download_Form()

    if request.method=='POST':
        form=Download_Form(request.POST)
        link = request.POST['link']
        video = YouTube(link)

        # setting video resolution
        # stream = video.streams.get_lowest_resolution()
        stream = video.streams.first().download()

        # downloads video
        # stream.download()
        return render(request,'testapp/download.html',{'stream':stream})
    return render(request,'testapp/download.html',{'form':form})

from django.shortcuts import render, redirect
from django.conf import settings
from .models import uploadFiles
from PIL import Image

def home(request):
    get_img = uploadFiles.objects.all().values()
    return render(request, './index.html', {
        'l': get_img,
        'title': 'Image upload assignment'
    })
def upload(request):
    if request.method == 'POST':
        myfile = request.FILES['files']
        root = settings.MEDIA_ROOT
        img = Image.open(myfile)
        size = (512,512)
        img.thumbnail(size)
        img.save(root+'/'+myfile.name)
        p = uploadFiles(fname=myfile.name, fileL=myfile.name)
        p.save()
        return redirect(home)
    return render(request, './upload.html', {
        'title': 'Upload Image'
    })

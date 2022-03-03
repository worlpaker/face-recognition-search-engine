from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .faces_train import check_face,new_check_face
import os


index_path = 'Face_recognition/index.html'

def index(request):
    global new_url
    if request.method == 'POST' and 'upload' in request.FILES:
        form = request.FILES['upload']
        test_path = 'Face_recognition/media/test'
        face_path = 'Face_recognition/media/test_faces/'
        fss = FileSystemStorage(location=os.path.join(settings.BASE_DIR, test_path))
        file = fss.save(form.name, form) 
        check_face(file) #train
        file_url = face_path + file
        new_url = file_url.replace('test_faces', 'test')
        Name = check_face.Face_name_is
        return render(request, index_path, {'file_url': file_url, 'Name': Name})
  
    if 'face_name' in request.POST:
        label = request.POST['face_name']
        new_path = f'Face_recognition/data/train/{label}'
        # check if file exist with same name
        if not os.path.exists(new_path):
         file_url = new_url.replace('test', 'test_faces')
         os.makedirs(new_path)
         os.rename(new_url, f"{new_path}/{label}.jpg")
         check_label ='success'
        # train
         new_check_face()
         return render(request, index_path, {'new_url': file_url, 'label': label, 'check_label': check_label})
        else:
            label = "already_saved"
        return render(request, index_path, {'label': label})

    return render(request ,index_path)     
        
 



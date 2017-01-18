from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from TestDjangoProject.settings import MEDIA_URL
import json
from models import FileDetails
# from forms import UploadFileForm
from django.core import serializers
# Create your views here.
@csrf_exempt
def save(request):
    if request.method =='POST':
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     file_field = request.FILES['datafile']
        #     print(file_field)
        #     # filehandler = request.POST'datafile')

        authorname = request.POST.get('authorname')
        fileHandler=request.FILES['dataFile']


        filepath = MEDIA_URL + fileHandler.name

        # file details methods
        # print(type(fileHandler))
        #
        # print (authorname)
        # print ("filepath :: ",filepath)
        # print (fileHandler.name)
        # print (fileHandler.size)
        # print(fileHandler.content_type)

        fileWriter = open(filepath, 'wb+')
        for chunk in fileHandler.chunks():
            fileWriter.write(chunk)
        fileWriter.close()

        # for reading file contents
        # for data in fileHandler:
        #     print(data)

        filename = fileHandler.name
        filetype = fileHandler.content_type
        data = FileDetails(fileName = filename, filePath = filepath, fileType = filetype, author = authorname)
        data.save()
        print(data)
    print("in view save")
    return HttpResponse(" Details Saved ")


def detailform(request):
    # form = UploadFileForm()
    # return render(request,'savedetail.html',{ 'form': form })
    return render(request, 'savedetail.html', {})

def home(request):
    data_list=[]
    for details in FileDetails.objects:
        data_list.append({'FileName':details.fileName,'FilePath':details.filePath,'FileType':details.fileType,'Author':details.author})
        print (data_list)
    return JsonResponse(data_list, safe=False)
    # data_serialised=serializers.serialize('json',data_list)
    # # return JsonResponse(data_serialised, safe=False)
    # # return HttpResponse(data_serialised,content_type='application/json')
    # return JsonResponse(data_serialised)


import json
import time
from .file_handler import read_file
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import User, Project, Input_headers, Output_headers
from .serializer import ProjectSerializer
from multiprocessing import Process
from threading import Thread


        

class ProjectAddList(viewsets.ModelViewSet):
    """
    this api adds and retrivesprojects
    """
    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse({'data':serializer.data}, safe=False)
    
    def create(self, request):
        file_fields = ['input_files', 'out_put_template', 'data_files']
        for f in file_fields:
            request.data[f] = [i.name for i in request.FILES.getlist(f)]
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project_documnet = serializer.save()
            for file_field in file_fields:
                p = Thread(target=read_file, args=[request.FILES.getlist(file_field), file_field, project_documnet.id])
                p.start()
                p.join()
                
            # print (project_documnet.id, 'lllllllllllllllllllllllllllll')
            return JsonResponse({'data':'project created successfully'}, status=201, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False, status=400)

class HeaderList(viewsets.ModelViewSet):
    """
    this api lists all the headers based on project
    """

    def list(self, request, project_id):
        data_dict = {}
        input_headers = Input_headers.objects.filter(project=project_id)
        # output_headers = Output_headers.objects.get(Project=project_id)
        for sheet in input_headers:
            data_dict['input_headers'] = {sheet.file_name: {sheet.sheet_name: None}}
            data_dict['input_headers'][sheet.file_name][sheet.sheet_name] = [i for i in sheet.headers.values()]
        # data_dict['output_headers'] = [i for i in output_headers.headrs.values()]
        return JsonResponse({'data': data_dict}, status=200)







            
        
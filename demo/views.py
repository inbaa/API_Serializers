from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverview(request):
    url={
        'jnj':'knjn',
        'njjjjn':"njnjnj",
    }
    return Response(url)

@api_view(['GET'])
def taskList(request):                              # Get all value
    tasks= Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, key):                         # Get a specific value
    tasks= Task.objects.get(id=key)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):                               # Create
    serializer= TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, key):                           # Update
    task =Task.objects.get(id=key)
    serializer= TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, key):                           # Delete
    task =Task.objects.get(id=key)
    task.delete()

    return Response("Item deleted!")
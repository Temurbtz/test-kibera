
from django.http import JsonResponse
from django.http import Http404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import New
from .serializers  import NewCreateSerializer,NewSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions  import IsOwner
from rest_framework.views import APIView
from rest_framework import generics
from .paginations import CustomPagination

class NewsListView(generics.ListCreateAPIView):
    queryset = New.objects.all().order_by('-date_created')
    serializer_class = NewSerializer
    pagination_class=CustomPagination

class CreateNewView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        data=JSONParser().parse(request)
        createserializer=NewCreateSerializer(data=data)
        if  createserializer.is_valid():
            new=createserializer.save(owner=request.user)
            getserializer=NewSerializer(new)
            return JsonResponse(getserializer.data, status=201)
        return JsonResponse(createserializer.errors, status=400)


class GetSingleNewView(APIView):
    def get(self,request,name=None):
        try:
            new=New.objects.get(name=name)
        except New.DoesNotExist:
            raise Http404
        serializer=NewSerializer(new)
        return Response(serializer.data)

class UpdateDestroyView(APIView):
    permission_classes=[IsAuthenticated,IsOwner]
    def put(self,request,name=None):
        try:
            new=New.objects.get(name=name)
        except New.DoesNotExist:
            raise Http404
        self.check_object_permissions(request,new)
        updateserializer = NewCreateSerializer(new, data=request.data)
        if  updateserializer.is_valid():
            new=updateserializer.save()
            getserializer=NewSerializer(new)
            return JsonResponse(getserializer.data, status=201)
        return JsonResponse(updateserializer.errors, status=400)
    def delete(self,request,name=None):
        try:
            new=New.objects.get(name=name)
        except New.DoesNotExist:
            raise Http404
        self.check_object_permissions(request,new)
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import  Response
from rest_framework.views import APIView

from .models import Status
from .serializers import StatusSerializer
from .reload import reset_status_call

class StatusView(APIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request):

        status = Status.objects.update( status= "False")

        reset_status_call(self)
        serializer = StatusSerializer(status)


        data = serializer.data

        return Response(data)



    def get(self, request):
        status = get_object_or_404(Status, pk=1)
        status_json = self.serializer_class(status)
        return Response(status_json.data)








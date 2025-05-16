from rest_framework import viewsets
from .models import TipoUser, LlaveSeguridad, SuperUser, Admin, Supervisor
from .serializers import (
    TipoUserSerializer, LlaveSeguridadSerializer,
    SuperUserSerializer, AdminSerializer, SupervisorSerializer
)

class TipoUserViewSet(viewsets.ModelViewSet):
    queryset = TipoUser.objects.all()
    serializer_class = TipoUserSerializer

class LlaveSeguridadViewSet(viewsets.ModelViewSet):
    queryset = LlaveSeguridad.objects.all()
    serializer_class = LlaveSeguridadSerializer

class SuperUserViewSet(viewsets.ModelViewSet):
    queryset = SuperUser.objects.all()
    serializer_class = SuperUserSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer
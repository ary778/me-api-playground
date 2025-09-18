# portfolio/views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the profile to be viewed or edited.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    # We override this method to ensure it always fetches the first profile
    def get_object(self):
        return Profile.objects.first()

    # We override this method to handle the list view (/api/profile/)
    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class HealthCheckView(APIView):
    def get(self, request, format=None):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
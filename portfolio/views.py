from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the profile to be viewed or edited.
    This will now show a list of all profiles at /api/profiles/
    and a single profile at /api/profiles/<pk>/
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# No need to override `get_object()` or `list()`
# The default `ModelViewSet` behavior automatically handles:
# - A list view (GET) by serializing the entire `queryset`
# - A detail view (GET, PUT, DELETE) by fetching a single object based on the URL's primary key (pk)

class HealthCheckView(APIView):
    def get(self, request, format=None):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
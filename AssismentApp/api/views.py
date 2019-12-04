

from rest_framework import viewsets
from AssismentApp.models import ReviewData
from AssismentApp.api.serializers import ReviewData_Serializer

class ReviewDataView(viewsets.ModelViewSet):
    queryset = ReviewData.objects.all()
    serializer_class = ReviewData_Serializer


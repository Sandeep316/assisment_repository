

from rest_framework import serializers
from AssismentApp.models import ReviewData

class ReviewData_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewData
        fields = '__all__'
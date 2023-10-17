from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from lms.serializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = '__all__'

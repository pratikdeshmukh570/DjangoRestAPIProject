from rest_framework import serializers
from api.models import Company, Employee, ExternalUser


# create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        id = serializers.ReadOnlyField()
        model = Employee
        fields = ['name', 'email', 'address', 'phone', 'about', 'position', 'company']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        id = serializers.ReadOnlyField()
        model = ExternalUser
        fields = ['name', 'user_Id', 'address', 'email', 'location', 'active']

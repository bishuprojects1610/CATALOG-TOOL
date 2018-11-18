from rest_framework_mongoengine import serializers
from .models import Project, User, Product, Input_headers, Output_headers, DataFiles


class ProjectSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProductSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class InputHeadersSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Input_headers
        fields = '__all__'

class DataFilesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = DataFiles
        fields = '__all__'

class OutputHeadersSerializer(serializers.DocumentSerializer):
    class Meta:
        model= Output_headers
        fields = '__all__'
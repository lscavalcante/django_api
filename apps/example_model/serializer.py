from rest_framework import serializers

from apps.example_model.models import ExampleModel


class ExampleModelSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=10)

    class Meta:
        model = ExampleModel
        fields = ['description']


class ExampleModelCreateTestSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=10)

    class Meta:
        fields = ['email']

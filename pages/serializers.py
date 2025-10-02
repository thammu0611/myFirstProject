from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        # or specify fields like this:
        # fields = ['id', 'title', 'description', 'completed']

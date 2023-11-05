from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
        # exclude=['user','image'] # egula chara bakigula show korbe 
        
    """ def save(self, **kwargs):
        kwargs['user'] = self.context['request'].user
        return super().save(**kwargs) """
    
    
""" class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPhoto
        fields = '__all__' """

""" class TaskSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    class Meta:
        model = Task
        fields = ['title','description','priority','photos','uploaded_images']
        
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        task = Task.objects.create(**validated_data)

        for image in uploaded_images:
            TaskPhoto.objects.create(task=task, image=image)

        return task """

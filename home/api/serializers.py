from rest_framework import serializers
from home.models import Category,Strories

class CategorySerial(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields =['id','create_date','update_date','slug'] 

class StroriesSerial(serializers.ModelSerializer):
    class Meta:
        model = Strories
        fields = '__all__'
    
class CategoryCreateSerial2(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.ImageField()

    def create(self, validated_data):
        data = Category.objects.create(**validated_data)
        return data
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.image = validated_data.get('image',instance.image)
        instance.save()
        return instance
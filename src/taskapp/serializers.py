
from .models import Contact

from rest_framework.serializers import(
    ModelSerializer,
    IntegerField,
    ReadOnlyField
)


class contactAppSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    #owner = ReadOnlyField(source='owner.username')
    class Meta:
        model = Contact
        fields = ('name','id')

    def create(self, validated_data):
        """
        Create and return a new `Contact` instance, given the validated data.
        """
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Contact` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
        

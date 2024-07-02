from django.contrib.auth.models import Group, User
from rest_framework import serializers
from  transformer.models import AmazonLabels

class AmazonLabelsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='transformer:label-highlight', format='html')

    class Meta:
        model = AmazonLabels
        fields = ['url', 'id', 'owner', 'highlight',
                  'label', 'cat_name', 'svg_str']
        extra_kwargs = {
            'url': {'view_name': 'transformer:label-detail', 'lookup_field': 'pk'}
        }
        
class UserSerializer(serializers.ModelSerializer):
    labels = serializers.HyperlinkedRelatedField(many=True, view_name='transformer:user-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url','id', 'username', 'labels']
        extra_kwargs = {
            'url': {'view_name': 'transformer:user-detail', 'lookup_field': 'pk'}
        }
        

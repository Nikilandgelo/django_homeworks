from rest_framework import serializers
from advertisements.models import Advertisement

class AdvertisementSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source = 'creator.username', read_only = True)

    class Meta:
        model = Advertisement
        fields = '__all__'
        read_only_fields = ['creator']  
    
    def create(self, validated_data):
        self.validate_status(Advertisement.StatusChoices.OPEN)
        validated_data['creator'] = self.context.get('request').user
        return super().create(validated_data)
    
    def validate_status(self, value):
        adverts_count = len(self.context.get('request').user.adverts.all().filter(status=Advertisement.StatusChoices.OPEN))
        if adverts_count >= 10 and value == Advertisement.StatusChoices.OPEN:
            raise serializers.ValidationError("У пользователя не может быть больше 10 открытых обьявлений")
        return value
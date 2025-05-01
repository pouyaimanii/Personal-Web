from rest_framework import serializers
from .models import (
    SocialLinksModel,
    UserSpecializationModel,
    AboutModel,
    ExperiencesModel,
    ContactMessage,
    Subscriber,
    PortfolioModel,
    SiteText,
    KnowledgeCategoryModel,
    KnowledgeModel,
    SiteImage
)


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinksModel
        fields = '__all__'


class UserSpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSpecializationModel
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = '__all__'


class ExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperiencesModel
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioModel
        fields = '__all__'


class SiteTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteText
        fields = '__all__'


class KnowledgeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeCategoryModel
        fields = '__all__'


class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeModel
        fields = '__all__'


class SiteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteImage
        fields = '__all__'
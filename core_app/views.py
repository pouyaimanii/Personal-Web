from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

from .serializers import (
    SocialLinksSerializer,
    UserSpecializationSerializer,
    AboutSerializer,
    ExperiencesSerializer,
    ContactMessageSerializer,
    SubscriberSerializer,
    PortfolioSerializer,
    SiteTextSerializer,
    KnowledgeCategorySerializer,
    KnowledgeSerializer,
    SiteImageSerializer
)

# Social Links
class SocialLinksAPIView(APIView):
    def get(self, request):
        social_links = SocialLinksModel.objects.first()
        serializer = SocialLinksSerializer(social_links)
        return Response(serializer.data, status=status.HTTP_200_OK)

# User Specializations
class UserSpecializationAPIView(APIView):
    def get(self, request):
        specializations = UserSpecializationModel.objects.all()
        serializer = UserSpecializationSerializer(specializations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# About
class AboutAPIView(APIView):
    def get(self, request):
        about = AboutModel.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Experiences
class ExperiencesAPIView(APIView):
    def get(self, request):
        experiences = ExperiencesModel.objects.all()
        serializer = ExperiencesSerializer(experiences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Contact Messages
class ContactMessageAPIView(APIView):
    def get(self, request):
        messages = ContactMessage.objects.all()
        serializer = ContactMessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
            name = request.data.get('name')
            phone_number = request.data.get('phone_number')
            email = request.data.get('email')
            subject = request.data.get('subject')
            message = request.data.get('message')
            ContactMessage.objects.create(name=name, phone_number=phone_number, email=email, subject=subject, message=message)
            return Response({'message : contact message created successfully.'}, status=status.HTTP_201_CREATED)
# Subscribers
class SubscriberAPIView(APIView):
    def get(self, request):
        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    def post(self, request):
            email = request.data.get('email')
            Subscriber.objects.create(email=email)
            return Response({'message': 'subscriber created successfully.'}, status=status.HTTP_201_CREATED)

# Portfolio
class PortfolioAPIView(APIView):
    def get(self, request):
        portfolios = PortfolioModel.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Site Texts
class SiteTextAPIView(APIView):
    def get(self, request):
        texts = SiteText.objects.all()
        serializer = SiteTextSerializer(texts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Knowledge Categories
class KnowledgeCategoryAPIView(APIView):
    def get(self, request):
        categories = KnowledgeCategoryModel.objects.all()
        serializer = KnowledgeCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Knowledge Items
class KnowledgeAPIView(APIView):
    def get(self, request):
        knowledge = KnowledgeModel.objects.all()
        serializer = KnowledgeSerializer(knowledge, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Site Images
class SiteImageAPIView(APIView):
    def get(self, request):
        images = SiteImage.objects.all()
        serializer = SiteImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

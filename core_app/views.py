from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    ProjectStatisticsModel,
    ExperienceYearsModel ,
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
    SiteImageSerializer,
    ProjectStatisticsSerializer,
    ExperienceYearsSerializer ,
)

class SocialLinksAPIView(APIView):
    def get(self, request):
        try:
            social_links = SocialLinksModel.objects.all()
            if not social_links:
                return Response({'error' : "social links not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = SocialLinksSerializer(social_links, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserSpecializationAPIView(APIView):
    def get(self, request):
        try:
            specializations = UserSpecializationModel.objects.all()
            if not specializations:
                return Response({'error' : "specializations not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSpecializationSerializer(specializations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    




class ProjectStatisticsAPIView(APIView):
    def get(self, request):
        try:
            projectStatistics = ProjectStatisticsModel.objects.all()
            if not projectStatistics:
                return Response({'error' : "projectStatistics not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = ProjectStatisticsSerializer(projectStatistics, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)    
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        





class ExperienceYearsAPIView(APIView):
    def get(self, request):
        try:
            experienceYear = ExperienceYearsModel.objects.first()
            if not experienceYear:
                return Response({'error' : "experienceYear not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = ExperienceYearsSerializer(experienceYear)
            return Response(serializer.data, status=status.HTTP_200_OK)            
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class AboutAPIView(APIView):
    def get(self, request):
        try:
            about = AboutModel.objects.all()
            if not about:
                return Response({'error' : "about not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = AboutSerializer(about, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)    
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

class ExperiencesAPIView(APIView):
    def get(self, request):
        try:
            experiences = ExperiencesModel.objects.all()
            if not experiences:
                return Response({'error' : "experiences not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = ExperiencesSerializer(experiences, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContactMessageAPIView(APIView):
    def get(self, request):
        try:
            messages = ContactMessage.objects.all()
            if not messages:
                return Response({'error' : "messages not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = ContactMessageSerializer(messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)    
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
    def post(self, request):
        try:
            name = request.data.get('name')
            if not name:
                return Response({'error' : "name not found."}, status=status.HTTP_404_NOT_FOUND)
            phone_number = request.data.get('phone_number')
            if not phone_number:
                return Response({'error' : "phone number not found."}, status=status.HTTP_404_NOT_FOUND)
            email = request.data.get('email')
            if not email:
                return Response({'error' : "email not found."}, status=status.HTTP_404_NOT_FOUND)
            subject = request.data.get('subject')
            if not subject:
                return Response({'error' : "subject not found."}, status=status.HTTP_404_NOT_FOUND)
            message = request.data.get('message')
            if not message:
                return Response({'error' : "message not found."}, status=status.HTTP_404_NOT_FOUND)
            ContactMessage.objects.create(name=name, phone_number=phone_number, email=email, subject=subject, message=message)
            return Response({'message : contact message created successfully.'}, status=status.HTTP_201_CREATED)        
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class SubscriberAPIView(APIView):
    def get(self, request):
        try:
            subscribers = Subscriber.objects.all()
            if not subscribers:
                return Response({'error' : "subscribers not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = SubscriberSerializer(subscribers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)        
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    


    def post(self, request):
        try:
            email = request.data.get('email')
            if not email:
                return Response({'error' : "email not found."}, status=status.HTTP_404_NOT_FOUND)
            Subscriber.objects.create(email=email)
            return Response({'message': 'subscriber created successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            

class PortfolioAPIView(APIView):
    def get(self, request):
        try:
            portfolios = PortfolioModel.objects.all()
            if not portfolios:
                return Response({'error' : "portfolios not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = PortfolioSerializer(portfolios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)            
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SiteTextAPIView(APIView):
    def get(self, request):
        try:
            texts = SiteText.objects.all()
            if not texts:
                return Response({'error' : "texts not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = SiteTextSerializer(texts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)            
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class KnowledgeCategoryAPIView(APIView):
    def get(self, request):
        try:
            categories = KnowledgeCategoryModel.objects.all()
            if not categories:
                return Response({'error' : "categories not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = KnowledgeCategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)            
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class KnowledgeAPIView(APIView):
    def get(self, request):
        try:
            knowledge = KnowledgeModel.objects.all()
            if not knowledge:
                return Response({'error' : "knowledge not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = KnowledgeSerializer(knowledge, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)    
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

class SiteImageAPIView(APIView):
    def get(self, request):
        try:
            images = SiteImage.objects.all()
            if not images:
                return Response({'error' : "images not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = SiteImageSerializer(images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


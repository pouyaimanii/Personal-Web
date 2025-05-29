from django.urls import path
from .views import (
    SocialLinksAPIView,
    UserSpecializationAPIView,
    AboutAPIView,
    ExperiencesAPIView,
    ContactMessageAPIView,
    SubscriberAPIView,
    PortfolioAPIView,
    SiteTextAPIView,
    KnowledgeCategoryAPIView,
    KnowledgeAPIView,
    SiteImageAPIView,
    ProjectStatisticsAPIView,
    ExperienceYearsAPIView
)

urlpatterns = [
    path('social-links/', SocialLinksAPIView.as_view(), name='social-links'),
    path('specializations/', UserSpecializationAPIView.as_view(), name='specializations'),
    path('project-statistics/', ProjectStatisticsAPIView.as_view(), name='project-statistics'),
    path('experience-years/', ExperienceYearsAPIView.as_view(), name='experience-years'),
    path('about/', AboutAPIView.as_view(), name='about'),
    path('experiences/', ExperiencesAPIView.as_view(), name='experiences'),
    path('contact-messages/', ContactMessageAPIView.as_view(), name='contact-messages'),
    path('subscribers/', SubscriberAPIView.as_view(), name='subscribers'),
    path('portfolios/', PortfolioAPIView.as_view(), name='portfolios'),
    path('site-texts/', SiteTextAPIView.as_view(), name='site-texts'),
    path('knowledge-categories/', KnowledgeCategoryAPIView.as_view(), name='knowledge-categories'),
    path('knowledges/', KnowledgeAPIView.as_view(), name='knowledges'),
    path('site-images/', SiteImageAPIView.as_view(), name='site-images'),
]

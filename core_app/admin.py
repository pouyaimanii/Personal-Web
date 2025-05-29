from django.contrib import admin

from .models import  ProjectStatisticsModel, ExperienceYearsModel ,SocialLinksModel, UserSpecializationModel, SiteText, SiteImage, Subscriber, ContactMessage, KnowledgeCategoryModel, KnowledgeModel, PortfolioModel, ExperiencesModel, AboutModel








class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(AboutModel, AboutAdmin)



class SocialLinksAdmin(admin.ModelAdmin):
    pass


admin.site.register(SocialLinksModel, SocialLinksAdmin)



class UserSpecializationAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserSpecializationModel, UserSpecializationAdmin)







class ProjectStatisticsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectStatisticsModel, ProjectStatisticsAdmin)







class ExperienceYearsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExperienceYearsModel, ExperienceYearsAdmin)








class KnowledgeCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(KnowledgeCategoryModel, KnowledgeCategoryAdmin)


class KnowledgeAdmin(admin.ModelAdmin):
    pass


admin.site.register(KnowledgeModel, KnowledgeAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    pass


admin.site.register(PortfolioModel, PortfolioAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subscriber, SubscriberAdmin)



class ContactMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContactMessage, ContactMessageAdmin)


class ExperiencesAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExperiencesModel, ExperiencesAdmin)




@admin.register(SiteText)
class SiteTextAdmin(admin.ModelAdmin):
    list_display = ['key', 'language', 'value']
    list_filter = ['language']
    search_fields = ['key', 'value']


@admin.register(SiteImage)
class SiteImageAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    search_fields = ['key', 'value']


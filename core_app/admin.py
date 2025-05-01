from django.contrib import admin

# Register your models here.
from .models import  SocialLinksModel, UserSpecializationModel, SiteText, SiteImage, Subscriber, ContactMessage, KnowledgeCategoryModel, KnowledgeModel, PortfolioModel, ExperiencesModel





@admin.register(SocialLinksModel)
class SocialLinksAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SocialLinksModel.objects.exists()        



class UserSpecializationAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserSpecializationModel, UserSpecializationAdmin)


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




# from django.contrib import admin

@admin.register(SiteText)
class SiteTextAdmin(admin.ModelAdmin):
    list_display = ['key', 'language', 'value']
    list_filter = ['language']
    search_fields = ['key', 'value']


@admin.register(SiteImage)
class SiteImageAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    # list_filter = ['language']
    search_fields = ['key', 'value']

# from django.contrib import admin
# from .models import LogoModel, SocialLinks

# class LogoAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return not LogoModel.objects.exists()

# class SocialLinksAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return not SocialLinks.objects.exists()

# # در اینجا از AppConfig استفاده می‌کنیم که اطمینان حاصل کنیم هر دو مدل در یک بخش قرار بگیرند
# class ManagementAdminSite(admin.AdminSite):
#     site_header = "پنل مدیریت"
#     site_title = "مدیریت سایت"
    
#     # تغییر گروه‌بندی در منو
#     def get_app_list(self, request):
#         app_list = super().get_app_list(request)
#         for app in app_list:
#             if app['name'] == 'تنظیمات':  # تغییر نام گروه
#                 app['models'] = [model for model in app['models'] if model['name'] == 'لوگو' or model['name'] == 'شبکه‌های اجتماعی']
#         return app_list

# # تغییرات در ساختار پنل ادمین
# admin.site = ManagementAdminSite()

# # ثبت مدل‌ها
# admin.site.register(LogoModel, LogoAdmin)
# admin.site.register(SocialLinks, SocialLinksAdmin)
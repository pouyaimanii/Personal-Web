### عکس های داینامیک درست شود


from django.db import models
from django.core.validators import FileExtensionValidator


class SocialLinksModel(models.Model):
    social_name = models.CharField(max_length=100)
    icon = models.FileField(
    upload_to='socialImage/',
    validators=[FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])]
    )
    link = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.social_name  

    class Meta:
        verbose_name = "شبکه‌های اجتماعی"
        verbose_name_plural = "شبکه‌های اجتماعی"





class UserSpecializationModel(models.Model):
    title = models.CharField(max_length=100)
    numberProject = models.CharField(max_length=10)
    icon = models.FileField(
    upload_to='icon/',
    validators=[FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])]
    )

    class Meta:
        verbose_name = "تخصص ها"
        verbose_name_plural = "تخصص ها"

    
    def __str__(self):
        return self.title  
    



    
class ProjectStatisticsModel(models.Model):
    title = models.CharField(max_length=100)
    numberProject = models.CharField(max_length=10)
    icon = models.FileField(
    upload_to='icon/',
    validators=[FileExtensionValidator(allowed_extensions=['svg', 'png', 'jpg', 'jpeg'])]
    )

    class Meta:
        verbose_name = "آمار پروژه ها "
        verbose_name_plural = "آمار پروژه ها"

    
    def __str__(self):
        return self.title  
    
class ExperienceYearsModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        verbose_name = "سال های تجربه "
        verbose_name_plural = "سال های تجربه"

    
    def __str__(self):
        return self.title  
    







class TextKeys(models.TextChoices):
    HELLO_TEXT = 'hello_text', 'متن سلام'
    NAME = 'name', 'نام'
    TITLE_JOB = 'title_job', 'عنوان کاری'
    ABOUT_DESCRIPTION_HERO = 'about_description_hero', 'توضیحات درباره من بخش هیرو سکشن'



    EMAIL = "email", "ایمیل"
    PHONE_NUMBER = "phone_number", "شماره تلفن"
    ADDRESS = "address", 'آدرس'
    FOOTER_TITLE = "footer_title", 'عنوان فوتر'


    CONTACT_SMALL_TITLE= "contact_small_title", 'عنوان کوچک تماس باما'
    CONTACT_BIG_TITLE = 'contact_big_title', 'عنوان بزرگ تماس باما'
    CONTACT_DESCRIPTION ='contact_description', 'توضیحات تماس باما'

    PORTFOLIO_TITLE = 'portfolio_title', 'عنوان نمونه کار'
    PORTFOLIO_DESCRIPTION = 'portfolio_description', 'توضیحات نمونه کار'

    EXPERIENCES_TITLE = 'experiences_title', 'عنوان تجربیات'

    ABOUT_SMALL_TITLE = 'about_small_title', 'عنوان کوچک بخش درباره ما'
    ABOUT_BIG_TITLE = 'about_big_title', 'عنوان بزرگ بخش درباره ما'
    ABOUT_DESCRIPTION = 'about_description', 'توضیحات بخش درباره ما'


class AboutModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()



    class Meta:
        verbose_name = "درباره من"
        verbose_name_plural = "درباره من"


    def __str__(self):
        return self.title

class ExperiencesModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    type_experiences = models.CharField(max_length=300)


    class Meta:
        verbose_name = "تجربه ها"
        verbose_name_plural = "تجربه ها"


    def __str__(self):
        return self.title





class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "خبرنامه"
        verbose_name_plural = "خبرنامه"
        # app_label = 'management'      


    def __str__(self):
        return self.email














class PortfolioModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField(null=True, blank=True)
    link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "نمونه کار ها"
        verbose_name_plural = "نمونه کار ها"
        # app_label = 'management'      

    
    def __str__(self):
        return self.title  



class SiteText(models.Model):
    key = models.CharField(
        max_length=100,
        choices=TextKeys.choices,
        unique=True
    )
    value = models.TextField()
    language = models.CharField(max_length=10, default='fa')

    class Meta:
        verbose_name = "متن های سایت"
        verbose_name_plural = "متن های سایت"
           

    


    def __str__(self):
        return f"{self.get_key_display()} [{self.language}]"
    


class KnowledgeCategoryModel(models.Model):
    title = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "دسته بندی نمودار "
        verbose_name_plural = "دسته بندی نمودار "
       

    
    def __str__(self):
        return self.title  



class KnowledgeModel(models.Model):
    title = models.CharField(max_length=200)
    percent = models.IntegerField()
    category = models.ForeignKey(KnowledgeCategoryModel,  related_name='charts', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "نمودار دانش"
        verbose_name_plural = "نمودار دانش"
           

    
    def __str__(self):
        return self.title  






class ImageKeys(models.TextChoices):
    LOGO = 'logo', 'لوگو'
    HERO = 'hero', 'عکس هیرو سکشن'
    ABOUT = 'about', 'عکس بخش درباره من'
    EXPERIENCES = 'experiences', 'عکس بخش تجربیات'






class SiteImage(models.Model):
    key = models.CharField(
        max_length=100,
        choices=ImageKeys.choices,
        unique=True
    )
    value = models.ImageField(upload_to="images/")


    class Meta:
        verbose_name = "عکس های سایت"
        verbose_name_plural = "عکس های سایت"
           

    


    def __str__(self):
        return f"{self.key}"
    

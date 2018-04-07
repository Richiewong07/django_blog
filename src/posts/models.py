from django.db import models
from django.urls import reverse

from django.db.models.signals import pre_save

from django.utils.text import slugify

from django.conf import settings

# Create your models here.
# USING SOMETHING CALLED MVC FRAMEWORK (MODEL VIEW CONTROLLER) LOOK IT UP


# CHANGES LOCATION OF UPLOAD, ADD IT TO MODEL
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length = 120)
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to = upload_location,
                              null = True,
                              blank = True,
                              width_field = "width_field",
                              height_field = "height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    content = models.TextField()    # TextField() IS USUALLY LONGER THAN CharField()
    updated = models.DateTimeField(auto_now = True,auto_now_add = False)        # auto_now EVERYTIME IT'S SAVED INTO THE DATABASE -> updated will be set
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)      # auto_now_add IS WHEN IT'S ADDED INTO DATABASE INITIALLY, ONLY SET 1 TIME (SAVE AND SET)

    def __str__(self):              # UNICODE TO RETURN TITLE IN ADMIN PAGE
        return self.title


    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})    # "details" IS "name" PARAMETER in URL
        # return "/posts/%s" %(self.id)

    # CHANGES THE ORDERING
    class Meta:
        ordering = ["-timestamp", "-updated"]




def create_slug(instance, new_slug = None):
    # SLUGIFY TITLE
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug

    # CHECK IS SLUG EXISTS
    qs = Post.objects.filter(slug = slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug = new_slug)
    return slug




# # SIGNAL RECEIVER --> ALLOWS YOU TO DO SOMETHING BEFORE MODEL IS SAVED --> EVERYTIME METHOD SAVED IS CALLED IT GOES RECEIVER FUNCTION
# # *args and **kwargs --> IF FUNCTION RECIEVED OTHER THINGS IT IS ADDED TO IT
#
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    # # slugify TURNS TITLE INTO A SLUG --> "TESTLA ITEM 1" TO "TESLA-ITEM-1"
    # slug = slugify(instance.title)
    # # CHECK TO SEE IF SLUG EXISTS
    # exists = Post.objects.filter(slug = slug).exists()
    # if exists:
    #     slug = "%s-%s" %(slugify(instance.title), instance.id)
    #
    # instance.slug = slug
#
#
# # (receiver, sender)
# send = model class
pre_save.connect(pre_save_post_receiver, sender=Post)


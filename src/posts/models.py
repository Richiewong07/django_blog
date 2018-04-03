from django.db import models
from django.urls import reverse

# Create your models here.
# USING SOMETHING CALLED MVC FRAMEWORK (MODEL VIEW CONTROLLER) LOOK IT UP


# CHANGES LOCATION OF UPLOAD, ADD IT TO MODEL
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length = 120)
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




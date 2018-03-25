from django.db import models

# Create your models here.
# USING SOMETHING CALLED MVC FRAMEWORK (MODEL VIEW CONTROLLER) LOOK IT UP

class Post(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField()    # TextField() IS USUALLY LONGER THAN CharField()
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)        # auto_now EVERYTIME IT'S SAVED INTO THE DATABASE -> updated will be set
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)      # auto_now_add IS WHEN IT'S ADDED INTO DATABASE INITIALLY, ONLY SET 1 TIME (SAVE AND SET)

    def __str__(self):              # UNICODE TO RETURN
        return self.title



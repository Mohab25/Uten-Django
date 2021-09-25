from django.db import models

class Panel(models.Model):
    image = models.ImageField()

    def __str__(self):
        return str(self.id)

class FirstBanner(models.Model):
    title = models.CharField(max_length=500) 
    subtitle = models.CharField(max_length=500) 
    description = models.TextField()
    btn_text = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title 


class GalleryItem(models.Model):
    title = models.CharField(max_length=500) 
    subtitle = models.CharField(max_length=500) 
    description = models.TextField()
    image = models.ImageField()
    image_name = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.title 

    class Meta:
        ordering=['id']


class SecondBanner(models.Model):
    call_to_action_head = models.TextField()
    call_to_action_message = models.TextField()
    btn_message = models.CharField(max_length=100)
    image = models.ImageField(default='')
    def __str__(self):
        return str(self.id) 

class ContactSection(models.Model):
    title = models.TextField()
    call_to_action = models.TextField()
    image = models.ImageField(default='')
    def __str__(self):
        return self.title 

class Footer(models.Model):
    logo = models.ImageField()
    logo_description = models.TextField()
    contact_info_title = models.TextField()
    contact_info_location = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=12)

    def __str__(self):
        return str(self.id)




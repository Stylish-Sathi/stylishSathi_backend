from django.db import models
from django.contrib.postgres.fields import ArrayField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.

# #Image Model 
# class Image(models.Model):
#     image = models.ImageField(upload_to='images/')

 #Salon Model   
class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)
class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)

    def compress_image(self, image):
        # Open the image using PIL

        img = Image.open(image)

        # Resize the image
        max_size = (800, 800)
        img.thumbnail(max_size)

        # Convert the image to RGB mode
        img = img.convert('RGB')

        # Create a buffer to hold the image data
        output_buffer = BytesIO()

        # Save the image to the buffer in JPEG format with quality 75
        img.save(output_buffer, format='JPEG', quality=75)

        # Set the buffer's file position to the beginning
        output_buffer.seek(0)

        # Create an InMemoryUploadedFile object from the buffer
        uploaded_image = InMemoryUploadedFile(output_buffer, 'ImageField', f'{image.name.split(".")[0]}.jpg', 'image/jpeg', output_buffer.getbuffer().nbytes, None)

        # Set the Salon object's image field to the compressed image
        self.image = uploaded_image

        # Save the Salon object
        self.save()

        # Return the compressed image
        return uploaded_image

class Salon(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    phone_numbers = ArrayField(models.CharField(max_length=15), blank=False)
    email = models.EmailField(max_length = 255)
    imageAlbum = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE)
    docsAlbum = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE)
from django.db import models
from django.contrib.postgres.fields import ArrayField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.

#Image Model 
class Image(models.Model):
    image = models.ImageField(upload_to='images/')

 #Salon Model   
class Salon(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    phone_numbers = ArrayField(models.CharField(max_length=15), blank=False)
    email = models.EmailField(max_length = 255)
    images = ArrayField(models.ImageField(upload_to='salon_images/'))
    documents = ArrayField(models.ImageField(upload_to='salon_documents/'))

    def compress_image(self, images):
        uploaded_image = []
        # Open the image using PIL
        for i in range(len(images)):

            img = Image.open(images[i])

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
            uploaded_image[i] = InMemoryUploadedFile(output_buffer, 'ImageField', f'{images[i].name.split(".")[0]}.jpg', 'image/jpeg', output_buffer.getbuffer().nbytes, None)

        # Set the Salon object's image field to the compressed image
        self.images = uploaded_image

        # Save the Salon object
        self.save()

        # Return the compressed image
        return uploaded_image
    
    def compress_documents(self, docs):
        uploaded_docs = []
        # Open the doc using PIL
        for i in range(len(docs)):

            doc = Image.open(docs[i])

            # Resize the docs
            max_size = (800, 800)
            doc.thumbnail(max_size)

            # Convert the image to RGB mode
            doc = doc.convert('RGB')

            # Create a buffer to hold the image data
            output_buffer = BytesIO()

            # Save the image to the buffer in JPEG format with quality 75
            doc.save(output_buffer, format='JPEG', quality=75)

            # Set the buffer's file position to the beginning
            output_buffer.seek(0)

            # Create an InMemoryUploadedFile object from the buffer
            uploaded_docs[i] = InMemoryUploadedFile(output_buffer, 'ImageField', f'{docs[i].name.split(".")[0]}.jpg', 'image/jpeg', output_buffer.getbuffer().nbytes, None)

        # Set the Salon object's docs field to the compressed image
        self.documents = uploaded_docs

        # Save the Salon object
        self.save()

        # Return the compressed image
        return uploaded_docs
from django.db.models import Model, ImageField, DateTimeField


class Image(Model):
    uploaded_image = ImageField(upload_to='uploaded/')
    converted_image = ImageField(upload_to='converted/')
    created_at = DateTimeField(auto_now_add=True)

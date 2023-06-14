from django.db.models.signals import pre_save
from io import BytesIO
from PIL import Image
from django.dispatch import receiver
from django.core.files.uploadedfile import InMemoryUploadedFile
from home.models import Strories,Category
from django.utils.text import slugify


# @receiver(pre_save, sender = Strories)
# def StoriesSignal(sender, instance, *args, **kwargs):
#     image = Image.open(instance.image)
#     image.thumbnail((800, 1200))
#     out  = BytesIO()
#     image.save(out, format='png')
#     out.seek(0)
#     resized_image = InMemoryUploadedFile(out, 'ImageField', f"{instance.image.name.split('.')[0]}.png", 'image/png', out.tell(), None)
#     instance.image = resized_image

@receiver(pre_save, sender = Category)
def CategorySignal(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.name)

@receiver(pre_save, sender = Strories)
def StroriesSignal(sender,instance,*args,**kwargs):
    instance.slug = slugify(f'{instance.title} {instance.id}')    
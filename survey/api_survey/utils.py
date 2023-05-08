import os
from django.utils import timezone

def rename_image(instance, filename):
    now = timezone.now()
    base_dir = 'employee'
    extension = os.path.splitext(filename)[1]
    new_filename = f"{instance.identity_card}-{now:%Y%m%d%H%M%S}{extension}"
    return os.path.join(base_dir, new_filename)

def rename_question_image(instance, filename):
    now = timezone.now()
    base_dir = 'question'
    extension = os.path.splitext(filename)[1]
    new_filename = f"{instance.code}-{now:%Y%m%d%H%M%S}{extension}"
    return os.path.join(base_dir, new_filename)
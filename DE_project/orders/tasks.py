# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def order_verified_send_mail(email, text):
         send_mail(
        'Hello, Dear friend',
        text,
        'de.transport123@gmail.com',
        [email],
        fail_silently=False,
    )
 
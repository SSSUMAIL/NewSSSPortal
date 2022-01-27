from celery import shared_task
from mainApp.models import Category, Post
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


User = get_user_model()


@shared_task
def mail_sender():
    categories = Category.objects.all()
    post_list = Post.objects.filter(datetime__range=[datetime.now() - timedelta(days=7), datetime.now()])

    for category in categories:
        emails = []
        category_emails = category.users.values('email')

        for item in category_emails:
            if item['email']:
                emails.append(item['email'])

        if emails:
            html = render_to_string(
                'newspaper/send_messages/sender_mail.html',
                {
                    'post_list': post_list,
                }
            )

            message = EmailMultiAlternatives(
                subject=f'DoNotReply: Here is the latest post from "{category.name}" category from last week!',
                from_email='news.portal@mail.com',
                to=emails,
            )
            message.attach_alternative(html, 'text/html')
            message.send()
            print('FROM TASKS: Email Has Been Sent Successfully! ')
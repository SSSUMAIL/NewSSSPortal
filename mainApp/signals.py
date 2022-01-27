from django.core.mail import EmailMultiAlternatives, mail_admins
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from mainApp.models import Post
from django.template.loader import render_to_string


@receiver(post_save, sender=Post)
def created_handler(sender, instance, created, **kwargs):
    instance_category = instance.postCategory.first()

    if instance_category and not created:
        post_id = instance.pk
        emails_in_dict = instance_category.subscribers.all().values('email')
        print(emails_in_dict)
        emails = []
       
        for user_email in emails_in_dict:
            emails.append(user_email['email'])
        print(emails)
        html = render_to_string(
            'mainApp/send_messages/message.html',
            {'post_id': post_id},
        )

        msg = EmailMultiAlternatives(
                subject=f'New Post has been added in your subscribed category "{instance_category}"',
                from_email='newsportal@mail.com',
                to=emails
            )

        msg.attach_alternative(html, 'text/html')
        msg.send()

        if created:
            subject = f'{instance.author.author} posted {instance.title}'
        else:
            subject = f'{instance.author.author} changed his/her post: {instance.title}'

        mail_admins(
            subject=subject,
            message=instance.text,
        )


@receiver(post_delete, sender=Post)
def notify_admins(sender, instance, **kwargs):
    subject = f'{instance.author.author} deleted {instance.title}'
   
    mail_admins(
        subject=subject,
        message=instance.text,
    )
    
    print(f'{instance.author.author} deleted {instance.title}')



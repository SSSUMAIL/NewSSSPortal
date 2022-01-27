import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from mainApp.models import Post
from datetime import timedelta, datetime

logger = logging.getLogger(__name__)


def my_job():
    # post_list = Post.objects.filter(dateCreation__range=[datetime.now() - timedelta(days=7), datetime.now()])
    latest_posts = Post.objects.order_by('-id')[:5]
    emails = []
    for email in latest_posts:
        emails.append(email.author.author.email)
    for post in latest_posts:
        

        html = render_to_string(
                'mainApp/send_messages/weekly_news.html',
                {
                    'latest_posts': latest_posts,
                }
            )
        cat = post.postCategory.first()
        message = EmailMultiAlternatives(
            subject=f'Here is your report about all posts from "{cat}"-category for last week!',
            from_email='newsportal@mail.com',
            to=emails,
        )
        message.attach_alternative(html, 'text/html')
        message.send()
        print('report sent!')


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after our job has run.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
  """
  This job deletes APScheduler job execution entries older than `max_age` from the database.
  It helps to prevent the database from filling up with old historical records that are no
  longer useful.
  
  :param max_age: The maximum length of time to retain historical job execution records.
                  Defaults to 7 days.
  """
  DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
  help = "Runs APScheduler."

  def handle(self, *args, **options):
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        my_job,
        trigger=CronTrigger(week="*/1"),  # Every week
        id="my_job",  # The `id` assigned to each job MUST be unique
        max_instances=1,
        replace_existing=True,
    )
    logger.info("Added job 'my_job'.")

    scheduler.add_job(
        delete_old_job_executions,
        trigger=CronTrigger(
            day_of_week="mon", hour="00", minute="00"
        ),  # Midnight on Monday, before start of the next work week.
        id="delete_old_job_executions",
        max_instances=1,
        replace_existing=True,
    )
    logger.info(
        "Added weekly job: 'delete_old_job_executions'."
    )

    try:
        logger.info("Starting scheduler...")
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("Stopping scheduler...")
        scheduler.shutdown()
        logger.info("Scheduler shut down successfully!")
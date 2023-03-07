import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't
# have to serialize the configuration object to
# child processes. - namespace='CELERY' means all
# celery-related configuration keys should
# have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


######################################################
######################################################
######################################################

app.conf.beat_schedule = {
    # Scheduler Name
    'get-posts-one-week': {
        # Task Name (Name Specified in Decorator)
        'task': 'get_instagram_posts',
        # Schedule
        # 'schedule': 20.0,  # in seconds
        'schedule': crontab(day_of_week=1, hour=0, minute=0),
        # Function Arguments
        'args': ("cristiano",)
    },
}

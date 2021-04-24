from django.utils import timezone
from datetime import datetime, date, timedelta


def get_current_datetime():
    return timezone.make_aware(datetime.now())


def get_current_date_path_name():
    return get_current_datetime().strftime('%Y-%m-%dT%H:%M:%S')


def user_avatar_directory_path(instance, filename):
    user = instance.user
    return f'user_profile_avatars/users/{user.id}/{get_current_date_path_name()}/{filename}'

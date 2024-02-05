
import django
from django.utils import timezone

from mailing_services.models import Mailing


from datetime import datetime

now = datetime.now().time()

mailing_time = Mailing.objects.get(time='12:05').time

print(now)
print(mailing_time)
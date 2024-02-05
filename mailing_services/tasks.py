from smtplib import SMTPException

from django.core.mail import send_mail
from config import settings
from config.celery import app
from mailing_services.models import MailingLogs, Mailing
from datetime import datetime




@app.task  # регистриуем таску
def sender_mailing():
    print('идет отправка')
    send_mailing()

    # url = 'sdasd'
    # obj = Person.objects.get_or_create(last_name=f'{time.time()}11111111111111111', first_name='1111')
    return "необязательная заглушка"


def send_mailing():
    now = datetime.now().date()
    print('я был  и тут')
    print(now)
    print(type(now))

    """Отправка рассылки и создание лога рассылки"""
    for mailing in Mailing.objects.filter(status='in_work'):
        if mailing.finish_date < now:
            mailing.status = 'stopped'
            mailing.save()
            continue
        message = mailing.message
        clients = mailing.client.all()
        for client in clients:
            try:
                send_mail(
                    subject=message.header,
                    message=message.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email]
                )
                mailing_log = MailingLogs(
                    data_time=datetime.now(),
                    status='Success',
                    server_response='Сообщение успешно отправлено',
                    mailing=mailing,
                )
                """"добавить в логи клиента которому не дошло"""
                print('otpravleno\n', mailing_log)
                mailing_log.save()

            except SMTPException:
                print('ne otpravleno')
                mailing_log = MailingLogs(
                    data_time=datetime.now(),
                    status='Failure',
                    server_response='Сообщение не отправлено!',
                    mailing=mailing,
                )
                mailing_log.save()
            with open("log_data.txt", "a") as file:
                file.write(mailing_log.status)
                file.write(mailing_log.server_response)

#coding: utf-8

from django.shortcuts import render, redirect
from models import Request
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail


def validate_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def landing_render(request):
    return render(request, 'index.html')


def send_request(request):
    errors = {}
    old_post = {"name": request.POST.get("name", False),
                "email": request.POST.get("email", False),
                "phone": request.POST.get("phone", False)}
    if not old_post.get("name"):
        errors['name'] = 'Введите ваше имя'
    if old_post.get("email"):
        if not validate_email(old_post.get("email")):
            errors['email'] = 'Введена некорректная почта'
    if not old_post.get("phone"):
        errors['phone'] = 'Введите ваш телефон'
    if errors:
        return render(request, 'index.html', {"old_post": old_post, "errors": errors})
    Request(name=old_post['name'], phone=old_post['phone'], email=old_post['email']).save()

    super_users = User.objects.filter(is_superuser=True)
    recipients = [super_user.email for super_user in super_users]
    if recipients == [u'']:
        recipients = [settings.EMAIL_HOST_USER]
    user_name = ""
    user_email = ""
    if request.method == 'POST':
        if request.POST["phone"]:
            if old_post['name']:
                user_name = u'Имя клиента: ' + old_post['name'] + '\n'
            if old_post['email']:
                user_email = u'Почта клиента: ' + old_post['email'] + '\n'
            message = user_name + user_email + u'Телефон клиента: ' + old_post['phone']
            send_mail(
                'Новая заявка c Наблюдай.Онлайн',
                message,
                settings.EMAIL_HOST_USER,
                recipients,
                fail_silently=False
            )
    return redirect('/')
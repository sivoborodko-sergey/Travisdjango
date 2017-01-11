from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have a valid email address.')

        account = self.model(
            email=self.normalize_email(email),
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password):
        account = self.create_user(email, password)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    class Meta:
        verbose_name_plural = 'Пользователи'

    email = models.EmailField('E-mail', unique=True)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=100)

    # информационные поля
    created_at = models.DateTimeField('Дата регистрации', auto_now_add=True)

    is_admin = models.BooleanField('Админ или нет', default=False, blank=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

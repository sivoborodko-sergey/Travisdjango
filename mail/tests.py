from django.test import TestCase
from django.core.mail import send_mail
from account.models import Account
from mail.models import Mail


class MailMethodTests(TestCase):
    def test_write_on_database(self):
        author = Account.objects.create(email='eamil@email.email', password='55')
        m = Mail.objects.create(message='Test', author=author, head='Head Test', recipient='xryssteam@gmail.com')
        self.assertEqual(type(m), Mail)

    def test_simple_test(self):
        self.assertEqual(5 == 5, True)

    def test_send_email(self):
        m = send_mail('Test', 'Test', 'from@mail.me',
                      ['xryssteam@g,ail.com'], fail_silently=False)
        self.assertEqual(m == 1, True)
from django.core.management.base import BaseCommand
from print4you.models import *
from django.contrib.auth.models import User

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = 'Seed database for testing and development'

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, **options):
        self.stdout.write('Seeding...')
        runSeeder(self, options['mode'])
        self.stdout.write('Done.')


def clearDatabase():
    """Deletes all the table data"""
    Order.objects.all().delete()
    Printout.objects.all().delete()
    Address.objects.all().delete()
    User.objects.all().delete()


def addUsers():
    User.objects.create_user(
        username='admin',
        email='superuser.admin@przykladowyemail.com',
        password='adminpassword',
        is_staff=True,
        is_superuser=True)

    User.objects.create_user(
        username='jan.kowalski',
        email='jan.kowalski@przykladowyemail.com',
        password='userpassword')

    User.objects.create_user(
        username='adam.nowak',
        email='adam.nowak@przykladowyemail.com',
        password='userpassword')


def addAddresses():
    user1 = User.objects.get(username='jan.kowalski')
    user2 = User.objects.get(username='adam.nowak')

    user1address = Address(
        first_name='Jan',
        last_name='Kowalski',
        email=user1.email,
        city='Warszawa',
        street='kolorowa',
        home_number='12/3',
        postal_code='01-493',
        telephone_number='123123123',
        user=user1
    )

    user2address = Address(
        first_name='Adam',
        last_name='Nowak',
        email=user2.email,
        city='Opole',
        street='oleska',
        home_number='50',
        postal_code='45-052',
        telephone_number='123456789',
        user=user2
    )

    user1address.save()
    user2address.save()


def addPrintouts():
    printout1 = Printout(
        is_color=False,
        is_gloss=True,
        quantity=15,
        size='10x15',
        image_file='user_prints/grapefruit-slice-332-332.jpg',
        price=123.4
    )

    printout2 = Printout(
        is_color=True,
        is_gloss=False,
        quantity=7,
        size='A3',
        image_file='user_prints/img_lights.jpg',
        price=32.1
    )

    printout1.save()
    printout2.save()


def addOrders():
    printout1 = Printout.objects.get(image_file='user_prints/grapefruit-slice-332-332.jpg')
    printout2 = Printout.objects.get(image_file='user_prints/img_lights.jpg')
    user1 = User.objects.get(email='jan.kowalski@przykladowyemail.com')
    user2 = User.objects.get(email='adam.nowak@przykladowyemail.com')
    address1 = Address.objects.get(user=user1)
    address2 = Address.objects.get(user=user2)
    address1.user = None
    address1.pk = None
    address2.user = None
    address2.pk = None
    address1.save()
    address2.save()

    order1 = Order(
        payment_method='karta',
        delivery_method='kurier',
        is_paid=True,
        cost=123.4,
        printout=printout1,
        address=address1,
        user=user1
    )

    order2 = Order(
        payment_method='blik',
        delivery_method='paczkomat',
        is_paid=True,
        cost=32.1,
        printout=printout2,
        address=address2,
        user=user2
    )

    order1.save()
    order2.save()


def runSeeder(self, mode=MODE_REFRESH):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """

    clearDatabase()
    if mode == MODE_CLEAR:
        return

    addUsers()
    addAddresses()
    addPrintouts()
    addOrders()

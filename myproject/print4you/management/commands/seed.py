from django.core.management.base import BaseCommand
from myproject.print4you.models import *
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

    def handle(self, *args, **options):
        self.stdout.write('Seeding...')
        run_seed(self, options['mode'])
        self.stdout.write('Done.')


def clearDatabase():
    """Deletes all the table data"""
    Printout.objects.all().delete()
    Address.objects.all().delete()
    Order.objects.all().delete()
    User.objects.all().delete()

def addUsers():
    usrers='TEMP'
    # address.save()
    # logger.info("{} address created.".format(address))
    # return address

def addAddresses():
    address='TEMP'

def addPrintouts():
    printout='TEMP'

def addOrders():
    order='TEMP'


def run_seed(self, mode=MODE_REFRESH):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """

    clearDatabase()
    if mode == MODE_CLEAR:
        return

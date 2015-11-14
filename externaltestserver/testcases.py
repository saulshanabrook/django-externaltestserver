from django.test import TransactionTestCase
from django.conf import settings


class ExternalLiveServerTestCase(TransactionTestCase):
    live_server_url = settings.EXTERNAL_TEST_SERVER

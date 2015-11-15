from django.core.management.base import BaseCommand
from django.test.testcases import LiveServerThread
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.test.runner import setup_databases


class Command(BaseCommand):
    help = 'Starts a server to use for integration tests'

    def add_arguments(self, parser):
        parser.add_argument('port', type=int)

        parser.add_argument(
            '--static',
            action='store_const',
            dest='static_handler',
            default=None,
            const=StaticFilesHandler,
            help='Transperently serve staticfiles assets')

    def handle(self, *args, **options):
        self.stdout.write('Setting up test databases....')

        setup_databases(
            verbosity=0,
            interactive=False,
            keepdb=True,
        )
        host = "0.0.0.0"
        port = options["port"]
        lst = LiveServerThread(
            host=host,
            possible_ports=[port],
            static_handler=options['static_handler']
        )
        self.stdout.write(
            'Starting live server on http://%s:%s...' % (host, port)
        )
        lst.run()
        raise lst.error

from django.core.management import BaseCommand, call_command

class Command(BaseCommand):
    help = "Create migrations, run migrations, and collect static files."

    def handle(self, *args, **options):
        call_command("makemigrations", "--check")
        call_command("migrate")
        call_command("collectstatic", "--noinput")

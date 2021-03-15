from django.apps import AppConfig


class FinalConfig(AppConfig):
    name = 'accounts'

    # For signals ====> profiles saving on creation
    def ready(self):
        import accounts.signals

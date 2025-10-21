from django.apps import AppConfig


class QuizConfig(AppConfig):
    print("Bonjour")
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz'

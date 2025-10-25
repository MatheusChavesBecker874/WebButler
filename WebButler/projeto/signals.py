from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os

@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    if os.environ.get("RENDER") == "true":
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123")
            print("✅ Superusuário 'admin' criado automaticamente após migrações.")
        else:
            print("ℹ️ Superusuário 'admin' já existe.")
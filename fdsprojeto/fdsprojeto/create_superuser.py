from django.contrib.auth import get_user_model
from django.db.utils import OperationalError
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fdsprojeto.settings")
django.setup()

User = get_user_model()

try:
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="professor",
            email="professor@gmail.com",
            password="professor123"
        )
        print("✅ Superusuário criado com sucesso!")
    else:
        print("ℹ️ O superusuário já existe, nada foi feito.")
except OperationalError:
    print("⚠️ Banco de dados ainda não está pronto. Rode as migrações primeiro.")

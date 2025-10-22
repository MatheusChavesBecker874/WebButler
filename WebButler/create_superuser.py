from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

User = get_user_model()

try:
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        print("✅ Superusuário 'admin' criado com sucesso!")
    else:
        print("ℹ️ Superusuário 'admin' já existe.")
except OperationalError:
    print("⚠️ O banco de dados ainda não está pronto. Ignorando criação do superusuário.")

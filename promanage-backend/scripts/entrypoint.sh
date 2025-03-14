#!/bin/sh

# Attendre que la base de données soit prête
echo "Waiting for PostgreSQL..."
./scripts/wait-for-db.sh

# Exécuter les migrations
python manage.py migrate


# Collecter les fichiers statiques (seulement en production)
if [ "$DEBUG" = "False" ]; then
    python manage.py collectstatic --noinput
fi

# Créer le superutilisateur
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$ADMIN_USERNAME', '', '$ADMIN_INIT_PASSWORD') if not User.objects.exists() else None" | python manage.py shell

# Démarrer le serveur
exec python manage.py runserver 0.0.0.0:8000

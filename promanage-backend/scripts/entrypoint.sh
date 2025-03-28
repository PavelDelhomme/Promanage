#!/bin/sh

# Activer le mode debug et sortir immédiatement en cas d'erreur
set -ex

# Attendre que la base de données soit prête
echo "Waiting for PostgreSQL..."
./scripts/wait-for-db.sh

# Créer le dossier static s'il n'existe pas
mkdir -p /app/static

# Collecter les fichiers statiques (seulement en production)
# if [ "$DEBUG" = "False" ]; then
    # python manage.py collectstatic --noinput
#fi
# Collecter les fichiers statiques
echo "Contenu du dossier static :"
ls -la /app/static

# Exécuter les migrations
echo "Applying migrations..."
python manage.py makemigrations --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

ls -l /app/
ls -l /app/templates

# Créer le superutilisateur SEULEMENT si la table existe
echo "Checking for superuser..."
if ["$(python manage.py shell -c 'from django.contrib.auth import get_user_model; print(get_user_model().objects.exists())' = "False" ]; then
    echo "Creating superuser..."
    python manage.py shell -c from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$ADMIN_USERNAME', '', '$ADMIN_INIT_PASSWORD')
else
    echo "Superuser already exists"
fi

# Démarrage du serveur
#exec python manage.py runserver 0.0.0:8000

exec "$@"

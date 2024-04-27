echo "Building the Project"

echo "Make Migrations"
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static Files"
python manage.py collectstatic --noinput --clear
echo "Building the Project"
python -m pip install -r requirements.txt

echo "Make Migrations"
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static Files"
python manage.py collectstatic --noinput --clear
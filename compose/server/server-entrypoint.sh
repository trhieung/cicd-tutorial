#!/bin/sh

until cd /app/services/server
do
    echo "Waiting for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


# python manage.py collectstatic --noinput

# # create super user
# until DJANGO_SUPERUSER_PASSWORD=admin \
# DJANGO_SUPERUSER_USERNAME=admin \
# DJANGO_SUPERUSER_EMAIL=admin@domain.com \
# python manage.py createsuperuser \
# --no-input
# do
#     echo "Waiting for creating admin account..."
# done

# until python ml_utils/pyscript/push_review_text_label.py
# do
#     echo "Waiting for pushing test data to server"
# done

# gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
python manage.py runserver 0.0.0.0:8000
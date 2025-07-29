startapp:
	@if [ -z "$(NAME)" ]; then \
		echo "❌ Debes especificar el nombre de la app: make startapp NAME=miapp"; \
	else \
		python3 manage.py startapp $(NAME); \
	fi

runserver:
	python3 manage.py runserver --settings=settings.local;

runserver-pod:
	python3 manage.py runserver --settings=settings.prod;

createsuperuser:
	python3 manage.py createsuperuser --settings=settings.local;

makemigrations:
	python manage.py makemigrations --settings=settings.local;

migrate:
	python manage.py migrate --settings=settings.local;

requirements:
	pip freeze > requirements.txt;
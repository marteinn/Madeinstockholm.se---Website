export ATOMICPRESS_SETTINGS=settings.prod

init:
	pip install -r requirements/local.txt
	mkdir uploads
	python manage.py create_db
	python manage.py prefill fill

run_dev:
	python manage.py runserver -a -d

run:
	python manage.py runserver

export:
	python manage.py exporter export

sync:
	python manage.py s3 sync


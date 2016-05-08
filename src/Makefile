export ATOMICPRESS_SETTINGS=settings.prod

init:
	pip install -r requirements/local.txt
	mkdir uploads
	python manage.py create_db
	python manage.py prefill fill
	python manage.py db stamp head

run_dev:
	python manage.py runserver -a -d

upgrade_db:
	python manage.py db update

run:
	python manage.py runserver

export:
	python manage.py exporter export
	open blog

sync:
	python manage.py s3 sync


# MadeInStockholm.se

This is the madeinstockholm.se website based on AtomicPress.


## Requirements

- Python 2.7


## Getting started

1. Install requirements

    `pip install -r src/requirements/local.txt`

1. Install frontend requirements

    ```
    cd frontend
    npm install
    npm install gulp
    gulp
    ```

1. Create database

    `python mange.py create_db`

1. (Optional) Add sample data

    `python manage.py prefill fill`

1. Start server

    `python manage.py runserver`

1. Open your `http://127.0.0.1:5000/` in your browser
1. Done!


## Usage

- Run application

    `python manage.py runserver`

- Run application (with admin and debug enabled)

    `python manage.py runserver -a -d`

- Generate static assets

    `python manage.py exporter export`

- Upload to S3

    `python manage.py s3 sync`

This project also ships with a makefile that contains a couple of helper commands:

- `make run_dev`
- `make run`
- `make sync`


## Contributing

Want to contribute? Awesome. Just send a pull request.

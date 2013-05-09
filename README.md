Madeinstockholm.se - Website
============================

MadeInStockholm.se website, written in Python and Flask. We decided to open this project as an example on how you can utilize flask+flask-admin as a static site generator and showcase a S3 deploy workflow.

# Requirement
You need to have Python, pip, virtualenv and node installed before proceeding.


# Installing

Clone repository

    git clone git@github.com:marteinn/Madeinstockholm.se---Website.git

Open

    cd Madeinstockholm.se---Website

Init virtualenv

    virtualenv .

Activate virtualenv

    source bin/activate

Install flask + related packages

    pip install -r requirements.txt


Install grunt+bower

    npm install

Install bower packages

    bower install

Copy bower packages

    grunt bower:install

Compile less and js files

    grunt

Copy and rename config.example.py to config.py

    cp ./mis/config.example.py ./mis/config.py

Copy and rename uploads.example folder

    cp -r ./mis/uploads.example ./mis/uploads

Install initial data

    python manage.py createdb -i

# Run

Run server

    python manage.py runserver -a -d
    
Now, open 127.0.0.1:5000 in your browser.

# Build

Generate static files

    python manage.py build
    
A folder called build has now been created in mis

# Deploy

Upload the files you just generated to aws.

    python manage.py deploy

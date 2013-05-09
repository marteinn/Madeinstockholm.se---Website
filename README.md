Madeinstockholm.se---Website
============================

MadeInStockholm.se website, written in Python and Flask.

Made sure you have python, node and virtualenv installed.


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

# Build

Generate static files

    python manage.py build

# Deploy

Deploy static files, make sure you run build first and you have all correct AWS settings in config.py

    python manage.py deploy

# Setup Instructions

In a new folder create a new virtual environment and activate
```
$ mkdir sumosurvey
$ virtualenv sumosurvey-env
$ source sumosurvey-env/bin/activate
```

Clone this repository and install requirements
```
$ git@github.com:Timmerop/sumosurvey.git
$ cd sumosurvey
$ pip install -r requirements.txt
```

Create the database
```
$ mysql -u root -p
$ CREATE DATABASE sumodemo_db;
$ CREATE USER 'sumodemo_user'@'localhost' IDENTIFIED BY 'sumodemo_password';
$ GRANT ALL PRIVILEGES ON *.* TO 'sumodemo_user'@'localhost';
$ FLUSH PRIVILEGES;
$ quit
```

Create superuser (follow the prompts)
```
$ python manage.py createsuperuser
```

Start the app
```
$ python manage.py runserver
```

Enjoy!
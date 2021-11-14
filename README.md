# Setup
Create Database in mysql. Ex. gutendex
```sh
mysql -u root -p
CREATE DATABASE gutendex;
```

> Note: import MySQL dump data in newly created gutendex database.

Get Project from Git
```sh
git clone ...this..repo..
```

Change DATABASES configuration of `bookstore/settings.py` file.
```sh
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'gutendex',
		'USER': 'mysql_user_name',
		'PASSWORD': 'mysql_password',
		'HOST': 'localhost',
		'PORT': '3306',
		'OPTIONS': {'charset': 'utf8mb4'},
	},
}
```

# Installation and Run Server
This will setup virtual environment, migrate the Database and run the server using `settings.py` file
```sh
source dj_run.sh
```

# Now you can test website
Open `http://127.0.0.1:8000/api/book/` URL in the brower (ex. Chrome)

You can filter data by
```sh
/api/book/?book_id=1260
/api/book/?language=en
/api/book/?mime_type=pdf
/api/book/?topic=Social
/api/book/?author=Thoreau
/api/book/?title=Buddhism
```

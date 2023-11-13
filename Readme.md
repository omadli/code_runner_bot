Code runner bot

# Installation
## Install python env and libraries

- In Windows:
```shell
$ pip install virtualenv
$ python -m venv venv
$ venv/Scripts/activate
$ pip install -r requirements.txt
```

- In Linux (like Ubuntu):

```shell
$ sudo apt install python3.11 python3-pip python3.11-venv
$ python3 -m pip install virtualenv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Configurate `.env` values
Copy from `.env.example` file and create `.env` file.
```shell
$ cp .env.example .env
```

Edit `.env` file values
```shell
$ nano .env
```
Values:
 - `BOT_TOKEN` - Bot token from [@botfather](https://t.me/botfather)
 - `DEBUG` - boolean True or False for debugging
 - `ADMINS` - list[int] bot admins's telegram id number
 - `DB_URL` - Database connection URL like postgresql or mysql (sqlite3 has asynchronous queries problem)
 - `USE_REDIS` - boolean: True or False if True use `redis` for caching
 - `REDIS_DB` - `redis` database number (if USE_REDIS is True)
 - `REDIS_PASSWORD` - `redis` database password (if USE_REDIS is True)

## Configure Database
Install and configure Postgresql or MySQL. Create schemas using these commands:
```shell
$ aerich init -t settings.TORTOISE_ORM
$ aerich init-db
```
Migrations:
```shell
$ aerich migrate
$ aerich upgrade
```

# Running bot
Running bot using this command:
```shell
$ python main.py
```
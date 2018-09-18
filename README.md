# glass

Welcome to glass, the pinfile viewer hosted at https://scribe.fluffybread.net!

Please drop an issue if you want to contribute to the site, and I'll give you some instructions.

# Requirements
* Python 3.5, would probably work in a later version
* PostgreSQL
* A working copy of the Scribe Discord bot, https://github.com/qxu21/scribe, which requires:
  * Python 3.5
  * discord.py rewrite (find instructions at https://discord.gg/r3sSKJJ)
  * asyncpg
* Alternatively, one could fake a Scribe installation (this section WIP):
  * create a postgres database called `scribe` by running the following commands in postgres, or in another way:
    * `create user USER with password 'PWD';`
    * `create database DB;`
    * `grant all privileges on database DB to USER;`
  * copy `demo_glass_config.py` to `config.py` and fill in your password and the directory in which you wish to store your fake pinfiles
* Python modules (pip install [name])
  * flask
  * flask-login
  * flask-sqlalchemy
  * psycopg2
* Apache 2 (I'll post the apache config file soon)

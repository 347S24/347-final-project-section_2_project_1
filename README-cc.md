scannerGallery
==============================

Final project for group2-1: a photo showcasing web app

### Quick setup

> The next steps assume that conda is already installed

1 - <a name="step-1">Create a conda environment:</a>


```bash
conda create python=3.8 -n scannergallery
```
2 - <a name="step-2">Activate the conda environment</a>

```bash
conda activate scannergallery
```

3 - <a name="step-3">Install the project basic dependencies and development dependencies</a>

> Make sure you are inside the root project directory before executing the next commands.
>
> The root project directory is the directory that contains the `manage.py` file

On Linux and Mac

```bash
pip install -r requirements/local.txt
```

On Windows

```bash
pip install -r requirements\local.txt
```

4 - <a name="step-4">Configure the database connection string on the .env</a>

On Linux and Mac

```bash
cp env.sample.mac_or_linux .env
```

On Windows

```bash
copy env.sample.windows .env
```

Change the value of the variable `DATABASE_URL` inside the file` .env` with the information of the database we want to connect.

Note: Several project settings have been configured so that they can be easily manipulated using environment variables or a plain text configuration file, such as the `.env` file.
This is done with the help of a library called django-environ. We can see the formats expected by `DATABASE_URL` at https://github.com/jacobian/dj-database-url#url-schema. 

5 - <a name="step-5">Use the django-extension's `sqlcreate` management command to help to create the database</a>

On Linux:

```bash
python manage.py sqlcreate | sudo -u postgres psql -U postgres
```

On Mac:

```bash
python manage.py sqlcreate | psql
```

On Windows:

Since [there is no official support for PostgreSQL 12 on Windows 10](https://www.postgresql.org/download/windows/) (officially PostgreSQL 12 is only supported on Windows Server), we choose to use SQLite3 on Windows

6 - <a name="step-6">Run the `migrations` to finish configuring the database to able to run the project</a>


```bash
python manage.py migrate
```


### <a name="running-tests">Running the tests and coverage test</a>


```bash
coverage run -m pytest
```


## <a name="troubleshooting">Troubleshooting</a>

If for some reason you get an error similar to bellow, is because the DATABASE_URL is configured to `postgres:///scannergallery` and because of it the generated `DATABASES` settings are configured to connect on PostgreSQL using the socket mode.
In that case, you must create the database manually because the `sqlcreate` is not capable to correctly generate the SQL query in this case.

```sql
ERROR:  syntax error at or near "WITH"
LINE 1: CREATE USER  WITH ENCRYPTED PASSWORD '' CREATEDB;
                     ^
ERROR:  zero-length delimited identifier at or near """"
LINE 1: CREATE DATABASE scannergallery WITH ENCODING 'UTF-8' OWNER "";
                                                             ^
ERROR:  syntax error at or near ";"
LINE 1: GRANT ALL PRIVILEGES ON DATABASE scannergallery TO ;
```



```sql
ERROR:  role "myuser" already exists
ERROR:  database "scannergallery" already exists
GRANT
```

<a name="troubleshooting-delete-database">You can delete the database and the user with the commands below and then [perform step 5 again](#step-5).</a>

> :warning: **Be very careful here!**: The commands below erase data, and should only be executed on your local development machine and **NEVER** on a production server.


On Linux:

```bash
sudo -u postgres dropdb -U postgres --if-exists scannergallery
sudo -u postgres dropuser -U postgres --if-exists myuser
```

On Mac:

```bash
dropdb --if-exists scannergallery
dropuser --if-exists myuser
```

We ran into some issues getting the droplet set up. As a result we were not able to have one key for Google OAuth and it only worked on Sarah's machine so in order to run the project you have to set up your own. Also, a person can remain signed in but lose permission to access google photos so the web page will crash if you try to load photos. The solution to this is to log out and log back in again. Users must log in with google because the site stores the photos on google photos.



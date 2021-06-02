# Game Club Admin Service

# This is a test project for EPAM Python [OnlineUA] Winter 2021 
Also, you can check specification of the project via `specification.pdf` file in project folder.
Here are the step-by-step tutorial make app run on your machine.

# Installation
Clone project to your folder and install required packages from `requirments.txt` or `Pipfile.lock` files
```
git init
git clone https://github.com/Kroll410/project_2
cd project_2

pip install -r requirements.txt 
    OR
pipenv install
```

# Database setup
Service uses MySQL database, so you need to install it.
Great MySQL installation tutorial is written [here](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

By default, service uses `root` name of the user, `12345` password and `project` as project name.
If it differs from yours, then you will have to change these three parameters in code.

Namely, in `config.py` in `Config` class variable `SQLALCHEMY_DATABASE_URI`, that by default is `'mysql+pymysql://root:12345@localhost/project'`
Change:
- `root` to your username
- `12345` to your password
- `project` to your database name

>> Also, if you changed the database name, you have to change the line in population SQL script.
In `sql/insert_data.sql` the first line: `USE project;` to `USE your_database_name;`

# Running the app

After installation all needed tools and requirements, you can start an app by using of these commands: 
- `python app.py`
- `flask run`




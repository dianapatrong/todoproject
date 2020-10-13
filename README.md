# To-do list
This project will resemble a to-do list where you can track all of the tasks that you need to complete, the user will be
able to create, update and delete tasks in the list. 

This basic application is written in Python, it uses Django web framework and Postgres as the database. 

## Django
Django runs on an Model View Template system:

**Model**: Sets out the schema for our database. With Django’s ORM, you can declare the fields, field types, etc. 

**View**: Set all of your code logic and algorithms, you can get results from the database or manipulate some data, it basically 
expects a request and a response. 

**Template**: Plain HTML code with Django's Template Language in it.

**Settings**: Holds all the settings of your web app.

**Url**: It helps to connect the view to a url.

**Admin**: Deals with how you want to view your models in the django admin.

## Setup local environment 

Install postgress


## CI/CD
**Travis CI** is a continuous integration service used to build and test applications hosted on GitHub. 
Travis CI supports integration with other tools such as coverage analyzers. In this case I used it 
to verify the integration of my code by an automated build which run the unit tests. 

The `.travis.yml` file was configured to use Python 3.7, install all needed dependencies, create a postgresql service, 
 along with a database that will only serve for testing purposes and finally the run of the unit tests.
Builds were configure to only run when a pull request is created. 

**Heroku** is a cloud platform that lets you build, deliver, monitor and scale applications. For this app, Heroku
was configure to deploy the application after a merge to master from a PR. 

Useful commands: 
* `heroku run bash -a todolist-dsti-devops` 
* `psql $DATABASE_URL`

## Infrastructure as Code
**Vagrant** is a tool for building and maintaining portable virtual software development environments, it 
also has integration with **Ansible** as a provisioner for these virtual machines. 

### Step-by-step: 
1. Install Virtualbox
2. Install Vagrant
3. Clone the repository `git clone git@github.com:dianapatrong/todoproject.git` and `cd todoproject`
4. Run: `vagrant up`
5. Wait for it to provision and the app will be running on: http://20.20.20.2:8000/


## ERRORS 
psql -h localhost -U postgres



Login as PostgreSQL Superuser "postgres" via "psql" Client
sudo -u postgres psql


ERROR: django.db.utils.ProgrammingError: permission denied for table django_migrations

https://stackoverflow.com/questions/38944551/steps-to-troubleshoot-django-db-utils-programmingerror-permission-denied-for-r

psql todo_proj -c "GRANT ALL ON ALL TABLES IN SCHEMA public to todouser;"
psql todo_proj -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to todouser;"
psql todo_proj -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to todouser;"
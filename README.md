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
Install requirements 

```
python manage.py migrate
export HOST=127.0.0.1
python manage.py runserver `
```

### Run unit tests
To run the unit tests: 

```
 $ export HOST=localhost
 $ python manage.py test
```

The output should be something like: 
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 0.312s

OK
Destroying test database for alias 'default'...
```

## CI/CD
**GitHub Actions** is a continuous integration that makes it easy to automate all your software workflows. 
It builds, test and deploys code right from GitHub.

> NOTE: I had used Travis CI but after a few issues with the provisioning of builds out of knowhere
> I decided to change to GitHub Actions

**Heroku** is a cloud platform that lets you build, deliver, monitor and scale applications. For this app, Heroku
was configure to deploy the application after a merge to master from a PR. 

For this project, the workflows are described in [.github/workflows](.github/workflows), there are two different types:
* Run unit tests: will only run only on Pull Requests and when a merge to master happens
* Deploy to Heroku: will be trigger only when there's a merge to master 


Useful commands: 
* `heroku run bash -a todolist-dsti-devops` 
* `psql $DATABASE_URL`

## Infrastructure as Code
**Vagrant** is a tool for building and maintaining portable virtual software development environments, it 
also has integration with **Ansible** as a provisioner for these virtual machines. 

To run the application make sure you have Virtualbox and Vagrant already installed and `cd` into the root directory
of the project: 
```
$ vagrant up
```
Wait for it to provision and the app will be running on: http://20.20.20.2:8000/ and http://localhost:8080/
this is because we have the following lines in the [Vagrantfile](Vagrantfile): 
```
server.vm.network :private_network, ip: "20.20.20.2"
server.vm.network "forwarded_port", guest: 8000, host: 8080, host_ip: "127.0.0.1"
```
* **private_network** allows to access the guest machine with a private address **20.20.20.2:8080**
* **forwarded_port** will allow accessing port **8000** on the guest via port **8080** on the host.

For the cleanup run: 
```
$ vagrant destroy
```
![Infrastructure as code architecutre](images/infra-as-code-architecture.png)
## Dockerizing the application

* [Dockerfile](Dockerfile) builds an image based on a Python image on Docker Hub, copies the code for the 
application and installs requierements. 

* [.dockerignore](.dockerignore)  excludes files and directories that match patterns in it.

* [docker-compose.yml](docker-compose.yml) describes the services that makes the application and the ports in which
the services will be exposed, in this case I have the **django web application** exposed on port **8000** and the
 postgres db exposed on port **5432**.

The image for the dockerfile can be found in **DockerHub** and can be downloaded via:
`docker pull patrondiana13/todolist-dsti-devops`

To run the application be sure to bee in the root directory of the project and execute the following commands: 
```
$ docker-compose build 
$ docker-compose up
```

> NOTE: `depends_on` does not wait for db to be "ready" before starting web - only until it's running

After that you can go to http://0.0.0.0:8000/ to test the application

For the cleanup run: 
```
$ docker-compose down
```

![Docker Architecture](images/docker-architecture.png)

## Kubernetes with Minikube
**Kubernetes** aims to provide a platform for automating deployment, scaling, and operations of application containers 
across clusters of hosts. It works with a range of container tools, including Docker.

**Minikube** is a tool that lets you run Kubernetes locally. Minikube runs a single-node Kubernetes cluster on your personal computer

To get started execute the following commands, make sure you are on the root directory of the project: 
````
$ minikube start --vm-driver=virtualbox
$ minikube dashboard
$ kubectl apply -f k8s/postgres
$ kubectl apply -f k8s/webapp
$ kubectl get services
$ minikube service django-service
````


The last command will open a browser with the application and the following info: 

````
|-----------|----------------|-------------|-----------------------------|
| NAMESPACE |      NAME      | TARGET PORT |             URL             |
|-----------|----------------|-------------|-----------------------------|
| default   | django-service |        8000 | http://192.168.99.105:32697 |
|-----------|----------------|-------------|-----------------------------|
🎉  Opening service default/django-service in default browser...
````

For the cleanup: 
```
$ kubectl delete -f k8s/postgres
$ kubectl delete -f k8s/webapp
$ minikube delete
```

## Service mesh using Istio

```
$ minikube start
$ curl -L https://istio.io/downloadIstio | sh -
$ cd istio-1.7.3
$ export PATH=$PWD/bin:$PATH
```

Return to the root directory of the project and deploy: 
``` 
$ cd ..
$ istioctl install --set profile=demo
$ kubectl label namespace default istio-injection=enabled
$ kubectl apply -f istio/postgres
$ kubectl apply -f istio/webapp 
```
Make sure there are no issues with the configuration: 
```
$ istioctl analyze 
✔ No validation issues found when analyzing namespace: default.
```

To know in which host is your application running to the following: 
```
$ minikube service todolist
```

> NOTE: When routing to different versions of the application I had to force refresh without cache in chrome, use 
> **Command** + **Shift** + **R**  if you are using a Mac; optionally you can open another browser. 

Istio can integrate with telemetry application to gain an understanding of the structure of the service mesh, 
display the topology and analyze the health of the mesh, following up we will deploy Kiali dashboard

```
$ kubectl apply -f istio-1.7.3/samples/addons
$ while ! kubectl wait --for=condition=available --timeout=600s deployment/kiali -n istio-system; do sleep 1; done
```

> NOTE: If there are errors trying to install the addons, try running the command again. There may be some timing 
> issues which will be resolved when the command is run again.

Access the Kiali dashboard
```
$ istioctl dashboard kiali
```

![Istio mesh](images/istio-mesh.png)

For the cleanup: 
```
$ kubectl delete -f istio/webapp
$ kubectl delete -f istio/postgres
$ minikube delete
```
## ERRORS 
psql -h localhost -U postgres
CREATE USER todouser WITH PASSWORD 'supersecretpassword' CREATEDB;
CREATE DATABASE todo_proj; 



Login as PostgreSQL Superuser "postgres" via "psql" Client
sudo -u postgres psql


ERROR: django.db.utils.ProgrammingError: permission denied for table django_migrations

https://stackoverflow.com/questions/38944551/steps-to-troubleshoot-django-db-utils-programmingerror-permission-denied-for-r

psql todo_proj -c "GRANT ALL ON ALL TABLES IN SCHEMA public to todouser;"
psql todo_proj -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public to todouser;"
psql todo_proj -c "GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to todouser;"


Creating test database for alias 'default'...
Got an error creating the test database: permission denied to create database

Kubernetes: 
 psql -d postgres -U todouser 
 todo_proj=# ALTER USER todouser CREATEDB; 

""

psql: error: could not connect to server: FATAL:  database "todouser" does not exist
su - postgres
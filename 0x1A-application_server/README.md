# 0x1A. Application server
##### `DevOps` `SysAdmin`

![c7d1ed0a2e10d1b4e9b3](https://github.com/samuelselasi/alx-system_engineering-devops/assets/85158665/2c883c9d-24a6-4d34-ac0b-e7fb86af802e)

### Background Context
Your web infrastructure is already serving web pages via `Nginx` that you installed in your [first web stack project](../0x0C-web_server). While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your `Nginx` and make is serve your Airbnb clone project.

## Resources
**Read or watch**:

* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (As mentioned in the video, do **not** install Gunicorn using `virtualenv`, just install everything globally)
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash](https://werkzeug.palletsprojects.com/en/0.14.x/routing/) in [route](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.route) - `strict_slashes`
* [Upstart documentation](https://doc.ubuntu-fr.org/upstart)

## Requirements
### General
* A `README.md` file, at the root of the folder of the project, is mandatory
* Everything Python-related must be done using `python3`
* All `config` files must have comments

## Bash Scripts
* All your files will be interpreted on Ubuntu `16.04` LTS
* All your files should end with a new line
* All your Bash script files must be executable
* Your Bash script must pass `Shellcheck` (version `0.3.7-5~ubuntu16.04.1` via `apt-get`) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

[0. Set up development with Python](./README.md)

Let’s serve what you built for [AirBnB clone v2 - Web framework](https://github.com/samuelselasi/AirBnB_clone_v2) on `web-01`. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

**Requirements**:

* Make sure that [task #3](0x0B-ssh/README.md) of your [SSH project](../0x0B-ssh) is completed for `web-01`. The checker will connect to your servers.
* Install the `net-tools` package on your server: `sudo apt install -y net-tools`
* Git clone your `AirBnB_clone_v2` on your `web-01` server.
* Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port `5000`.
* Your Flask application object must be named `app` (This will allow us to run and check your code).
**Example**:

##### Window 1:
```
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
```
##### Window 2:
```
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```

[1. Set up production with Gunicorn](./README.md)

Now that you have your development environment set up, let’s get your production application server set up with `Gunicorn` on `web-01`, port `5000`. You’ll need to install `Gunicorn` and any libraries required by your application. Your `Flask` application object will serve as a WSGI entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.

**Requirements**:

* Install `Gunicorn` and any other libraries required by your application.
* The Flask application object should be called `app`. (This will allow us to run and check your code)
* You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a `Gunicorn` instance to localhost listening on port `5000` with your application object as the entry point.
* In order to check your code, the checker will bind a `Gunicorn` instance to port `6000`, so make sure nothing is listening on that port.

**Example**:
##### Terminal 1:

```
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
[2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
[2019-05-03 20:47:20 +0000] [3595] [INFO] Using worker: sync
[2019-05-03 20:47:20 +0000] [3598] [INFO] Booting worker with pid: 3598
```
##### Terminal 2:

```
ubuntu@229-web-01:~$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~$
```

[2. Serve a page with Nginx](./2-app_server-nginx_config)

Building on your work in the previous tasks, configure `Nginx` to serve your page from the route `/airbnb-onepage/`

**Requirements**:

* `Nginx` must serve this page both locally and on its public IP on port `80`.
* `Nginx` should proxy requests to the process listening on port `5000`.
* Include your `Nginx` config file as `2-app_server-nginx_config`.

**Notes**:

* In order to test this you’ll have to spin up either your production or development application server (listening on port `5000`)
* In an actual production environment the application server will be configured to start upon startup in a system initialization script. This will be covered in the advanced tasks.
* You will probably need to `reboot` your server (by using the command `$ sudo reboot`) to have Nginx publicly accessible

**Example**:

### On my server:
#### Window 1:
```
ubuntu@229-web-01:~/AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-06 20:43:57 +0000] [14026] [INFO] Starting gunicorn 19.9.0
[2019-05-06 20:43:57 +0000] [14026] [INFO] Listening at: http://0.0.0.0:5000 (14026)
[2019-05-06 20:43:57 +0000] [14026] [INFO] Using worker: sync
[2019-05-06 20:43:57 +0000] [14029] [INFO] Booting worker with pid: 14029
```
### Window 2:
```
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```
### On my local terminal:
```
vagrant@ubuntu-xenial:~$ curl -sI 35.231.193.217/airbnb-onepage/
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 06 May 2019 20:44:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: keep-alive
X-Served-By: 229-web-01

vagrant@ubuntu-xenial:~$ curl 35.231.193.217/airbnb-onepage/
Hello HBNB!vagrant@ubuntu-xenial:~$
```


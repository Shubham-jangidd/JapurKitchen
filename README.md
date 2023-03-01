# Welcome to JaipurKitchen!

### Table of content
1. [Introduction](#introduction)
2. [Getting Started with development](#Getting-started-with-local-development)
		- [Pre-requisite](#pre-requisite)
		- [Steps to run the project](#Steps-to-run-the-project)
3. [Pages & Features of this webapplication](#Pages-&-Features-of-this-webapplication)
4. [AWS deployment of JaipurKitchen](#AWS-deployment-of-JaipurKitchen)
5. [Screenshots](#Screenshots)
6. [Future Scope & Improvements](#Future-Scope-&-Improvements)




## Introduction
 **JaipurKitchen** is a webapplication developed in python django. This web application gives users information about the different varity of food and best recommended places.

This webapplication is using following technologies.
1. Python3.6
2. Django 4.1.7
3. MySQL / SQlite for storing data.
4. JavaScript
5. Bootstrap
6. HTML

You can access this application live @ - http://jaipur-kitchen-140589185.ap-northeast-1.elb.amazonaws.com/

**Infrastructure** - Currently this application is hosted in AWS
- We are using EC2 to host the application code.
- this ec2 has nginx install which is acting as reverse proxy for django server
- There is a Loadbalancer in front of this ec2 machine which is entrypoint for our server.
- We are using RDS (MySQL) to store all sorts of data.


## Getting started with local development
#### **Pre-requisite :**
-   virtualenv
-   python3
-   MySQL v8.0.3 on local machine

#### **Steps to run the project**.

1.  Clone the project  `git clone https://github.com/Shubham-jangidd/JapurKitchen.git`
2.  cd JapurKitchen
3.  Update  `JapurKitchen/settings/development.py`  with mysql settings.
4.  virtualenv env
5.  source env/bin/activate
6.  pip3 install -r requirements.txt
7.  python3 manage.py migrate (only when setting up for first time.)
8.  python3 manage.py runserver

**Check the site on localhost:8000**

## Pages & Features of this webapplication
1. Homepage - **/** - This is the homepage / landing page when user opens the application.
2. About - **/about** - This page provided information about the website
3. contact - **/contact** -  This page contains a contact-us form. User can send queries and they will be stored into our database.
4. Signup - **/Signup** - This page allows user to register themselves into the platform.
5. Login - **/login** - Existing users can login in the webapp.
6. admin - **/admin** - It reads metadata from the database to provide a quick, model-centric interface where trusted users can manage content on the site.


## AWS deployment of JaipurKitchen
![enter image description here](https://raw.githubusercontent.com/Shubham-jangidd/JapurKitchen/main/images/jaipur-kitchen-draw-io.jpg)

## Screenshots
#### Homepage / Landing Page of webapp
![Homepage](https://raw.githubusercontent.com/Shubham-jangidd/JapurKitchen/main/images/Screenshot%202023-03-01%20at%2011.03.12%20PM.png)

#### About US
![AboutUS](https://raw.githubusercontent.com/Shubham-jangidd/JapurKitchen/main/images/Screenshot%202023-03-01%20at%2011.14.24%20PM.png)

#### Contact US
![contact us](https://raw.githubusercontent.com/Shubham-jangidd/JapurKitchen/main/images/Screenshot%202023-03-01%20at%2011.14.45%20PM.png)

#### User Login
![Login](https://raw.githubusercontent.com/Shubham-jangidd/JapurKitchen/main/images/Screenshot%202023-03-01%20at%2011.15.14%20PM.png)

#### User Registration
![Signup](https://raw.githubusercontent.com/Shubham-jangidd/JapurKitchen/main/images/Screenshot%202023-03-01%20at%2011.15.24%20PM.png)

#### Admin Panel
![Admin Panel](https://raw.githubusercontent.com/Shubham-jangidd/JapurKitchen/main/images/Screenshot%202023-03-01%20at%2011.27.25%20PM.png)




## Future Scope & Improvements

#### Application

 - [ ] Forgot / Reset Password
 - [ ] User Profile Section
 - [ ] Online ordering
 - [ ] Implement circuit breakers to avoid downtimes
 - [ ] Authentication
	 - [x] Email
	 - [ ] Mobile
	 - [ ] Social media login
 
 - [ ] SEO

#### Infrastructure

 - [ ] Use Autoscaling groups for scaling instead of ec2
 - [ ] Use S3 for storing images instead of ec2
 - [ ] Use Cloudfront to serve images for better performance
 - [ ] Use caching services like Redis to boost application performance.
 - [ ] Implement aws WAF to protect against malicious attackers.
 - [ ] Implement SSL currently application is running on port 80.


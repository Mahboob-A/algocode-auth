                         
<br/>
<div align="center">
<a href="https://github.com/Mahboob-A/algocode">
<img src="https://github.com/Mahboob-A/algocode/assets/109282492/cc00166b-bd56-4aca-8022-33928007c32e" alt="Logo" width="700" height="400">
</a>
<h3 align="center">Algocode - The Leetcode for Hackers</h3>
<p align="center">
Algocode is a DSA practice platform just like Leetcode!
<br/>
<br/>
<a href="https://github.com/Mahboob-A/algocode-auth"><strong>Read the blog »</strong></a>
<br/>
<br/>
<a href="https://github.com/Mahboob-A/algocode-auth">Algocode Auth Service .</a>  
<a href="https://github.com/Mahboob-A/code-manager">Code Manager Service .</a>
<a href="https://github.com/Mahboob-A/rcee/">RCE Engine Service</a>
</p>
</div>

<h3 align="center">General Information</h3>

Algocode is an online data structure and algorithm practice backend built in microservices architecture. 


*Algocode currently has three services*: <a href="https://github.com/Mahboob-A/algocode-auth">Algocode Auth Service .</a> <a href="https://github.com/Mahboob-A/code-manager">Code Manager Service .</a> and <a href="https://github.com/Mahboob-A/rcee/">RCE Engine Service</a>
<br/> <br/>

`Algocode Auth` is responsible for User Management service for `Algocode - a DSA Practice Platform just like Leetcode`. 

To learn more about Algocode, please `READ-THE-BLOG-URL` or visit <a href="https://github.com/Mahboob-A/algocode">Algocode</a> here. 

Algocode Auth Service uses `celery` to asynchronously send email to users,`Flower` to monitor `celery workers`,  `resend` for email service, and the auth service is a `fully dockerized solution`.

To read more on `Development` or `Production` stage, please follow the below sections.  

#### _NOTE_

**Workflow** 

Once a user completes a registration in the Algocode platfrom, a _profile_  for the user is also created of the user using **Django Signals**

**Documentation**

Please visit <a href="https://cm-doc.algocode.site/doc/">this documentation page</a>  for the detailed guide on Algocode Auth Service.

> However, all the APIs are referenced in the **_API Reference_** section below.

<br/> <br/><details>
<summary><h3 align="center">Development Stage</h3></summary>

#### Development Stage of Auth Service

The Algocode Auth Services uses the following services to serve the request during Development Stage.  

    a. Nginx as webserver.
    b. Gunicorn  as application server .
    c. Celery to process tasks asynchronously.
    d. Flower to monitor celery worker.
    e. Mailhog to mock email management.

<br/>
<br/>  

</details><details>
<summary><h3 align="center">Production Stage</h3></summary>

#### Production Stage of Auth Service

The Algocode Auth Services uses the following services to serve the request during Production Stage.  

    a. Nginx as webserver.
    b. Nginx Proxy Manager to manage Nginx.
    c. Portainer to manage and monitor docker container in Auth Service. 
    b. Gunicorn as application server.
    c. Celery to process tasks asynchronously.
    d. Flower to monitor celery worker.
    e. Resend as email service.

#### Deployment

The Auth Service is deployed in Azure VM 22.04 Ubuntu Server. 

<br/>
<br/>  

</details><details>
<summary><h3 align="center">API Reference - User Management</h3></summary>

Algocode uses JWT tokens as cookies to manage Authentication/Authorization token.

#### User Management APIs

##### Registration 

```http
    POST https://auth.algocode.site/api/v1/auth/registration/
```

| Parameter | Type     |        Description                |
| :-------- | :------- | :------------------------- |
| `username`    | `string` | **Required** Your username for the account.  |
| `email`    | `string` | **Required** Your valid email address.|
| `password1`   | `string` | **Required** Your password. | 
| `password2` | `string` |  **Required** Confirm your password. | 
| `first_name` | `string` | **Required**  Your first name. | 
| `last_name` | `string` | **Required** Your last name. | 

##### Login 

```http
  POST https://auth.algocode.site/api/v1/auth/login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`    | `string` |  `Your registered email.`  |
| `password` | `string` | `Your password.`|


##### Verify Email

```http
    POST  https://auth.algocode.site/api/v1/auth/registration/verify-email/
```

| Parameter | Type     |  Description                |
| :-------- | :------- | :------------------------- |
| `key`    | `string` | **Required**. Your copied token from your email  |

To learn more on **Registration APIs** please also visit here - <a href="https://github.com/Mahboob-A/algocode?tab=readme-ov-file#b-by-registering-in-the-algocode-platform/">Registration in Algocode</a> 

##### Change Password  _(While Authenticated)._

```http
    POST  https://auth.algocode.site/api/v1/auth/password/change/
```

| Parameter | Type     |  Description                |
| :-------- | :------- | :------------------------- |
| `new_password1`    | `string` | **Required**. Your new password. |
| `new_password2`    | `string` | **Required**. Confirm your new password.  |


##### Reset Password  _(Forgot Password)._  

```http
    POST  https://auth.algocode.site/api/v1/auth/password/reset/
```

| Parameter | Type     |  Description                |
| :-------- | :------- | :------------------------- |
| `email`    | `string` | **Required**. Your registered email |

##### Confirm Reset Password  _(Confirm Forgot Password)._  

```http
    POST  https://auth.algocode.site/api/v1/auth/password/reset/confirm/
```

| Parameter | Type     |  Description                |
| :-------- | :------- | :------------------------- |
| `token`    | `string` | **Required**. Token from the email sent to your registered email address. |
| `uid`    | `string` | **Required**.  UID from the email sent to your registered email address. |
| `new_password1`    | `string` | **Required**. Your new password. |
| `new_password2`    | `string` | **Required**. Confirm your new password.  |

##### Refresh Token  _(While Authenticated)._

```http
    POST  https://auth.algocode.site/api/v1/auth/token/refresh/
```

##### Refresh Token  _(While Authenticated)._

```http
    POST  https://auth.algocode.site/api/v1/auth/logout/
```

<br/>
<br/>  

</details><details>
<summary><h3 align="center">API Reference - User Details</h3></summary>


#### User Details APIs

##### Get All User Details 

```http
    GET  https://auth.algocode.site/api/v1/user/user-detail/
```

##### Get User Details of a User  

```http
    GET  https://auth.algocode.site/api/v1/user/user-detail/<uuid:id>/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`    | `string` |  **Required** The `id` of the user to get details  |

<br/>
<br/>  

</details><details>
<summary><h3 align="center">API Reference - Profile Details</h3></summary>


#### User Profile Details APIs

Profiles are the more user centric details for a user.

##### Get All User Profile Details 

```http
    GET  https://auth.algocode.site/api/v1/profile/all-user-profiles/
```

##### Get Profile Details of a User  _(Authenticated)_

```http
     GET  https://auth.algocode.site/api/v1/profile/profile/
```

##### Get Profile Details of other User  

```http
     GET  https://auth.algocode.site/api/v1/profile/profile/<uuid:id>/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`    | `string` |  **Required** The `id` of the user to get details  |

##### UPDATE Profile Details of a User  _(Authenticated)_

```http
     GET  https://auth.algocode.site/api/v1/profile/profile/update/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `gender`    | `string` |   `M`,  for  Male  `F` for Female , or `O` for Other. |
| `twitter_handle`    | `string` |   `Twitter` handle of the user. |
| `phone_number`    | `string` |  Phone number of the user.|

Please visit <a href="https://cm-doc.algocode.site/doc/">the documentation page</a>  for more details.

<br/>
<br/>  

</details><details>
<summary><h3 align="center">Run Locally and Contribution</h3></summary>

#### Run Locally

Please `fork` and `clone` this <a href="https://github.com/Mahboob-A/algocode-auth/tree/development/">development branch</a> of Algocode Auth Service, and follow along with the `envs-examples`. 

`cd` to `src` and create a `virtual environment`. Activate the virtual environment. 

Run `make docker-up` and the development setup will start running. Please install `make` in your host machine. 

If you use `Windows` Operating System, please run the  respective `docker commands` from the **`dev.yml`** docker compose file.

#### Contribution 

You are always welcome to contribute to the project. Please `open an issue` or `raise a PR` on the project.  

<br/>
<br/>  

</details><br/>

<a href="https://www.linux.org/" target="blank">
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="Linux" height="40" width="40" />
</a>
<a href="https://postman.com" target="blank">
<img align="center" src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="Postman" height="40" width="40" />
</a>
<a href="https://www.w3schools.com/cpp/" target="blank">
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="C++" height="40" width="40" />
</a>
<a href="https://www.java.com" target="blank">
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="Java" height="40" width="40" />
</a>
<a href="https://www.python.org" target="blank">
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" height="40" width="40" />
</a>
<a href="https://www.djangoproject.com/" target="blank">
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="Django" height="40" width="40" />
</a>
<a href="https://aws.amazon.com" target="blank">
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="AWS" height="40" width="40" />
</a>
<a href="https://www.docker.com/" target="blank">
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="Docker" height="40" width="40" />
</a>
<a href="https://www.gnu.org/software/bash/" target="blank">
<img align="center" src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="Bash" height="40" width="40" />
</a>
<a href="https://azure.microsoft.com/en-in/" target="blank">
<img align="center" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="Azure" height="40" width="40" />
</a>
<a href="https://circleci.com" target="blank">
<img align="center" src="https://www.vectorlogo.zone/logos/circleci/circleci-icon.svg" alt="CircleCI" height="40" width="40" />
</a>
<a href="https://nodejs.org" target="blank">
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="Node.js" height="40" width="40" />
</a>
<a href="https://kafka.apache.org/" target="blank">
<img align="center" src="https://www.vectorlogo.zone/logos/apache_kafka/apache_kafka-icon.svg" alt="Kafka" height="40" width="40" />
</a>
<a href="https://www.rabbitmq.com" target="blank">
<img align="center" src="https://www.vectorlogo.zone/logos/rabbitmq/rabbitmq-icon.svg" alt="RabbitMQ" height="40" width="40" />
</a>
<a href="https://www.nginx.com" target="blank">
<img align="center" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="Nginx" height="40" width="40" />
</a>
<br/>

#### 🔗 Links


[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/i-mahboob-alam/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/iMahboob_A)
<br/>
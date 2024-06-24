                         
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
<a href="https://imehboob.medium.com/my-experience-building-a-leetcode-like-online-judge-and-how-you-can-build-one-7e05e031455d"  target="_blank" ><strong>Read the blog »</strong> </a>
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

To learn more about _Algocode and the architecture_, please `READ-THE-BLOG-URL` or visit <a href="https://github.com/Mahboob-A/algocode">Algocode</a> here. 

Algocode Auth Service uses `celery` to asynchronously send email to users,`Flower` to monitor `celery workers`,  `resend` for email service, and the auth service is a `fully dockerized solution`.

To read more on `Development` or `Production` stage, please follow the below sections.  

#### _NOTE_

**Workflow** 

Once a user completes a registration in the Algocode platfrom, a _profile_  for the user is also created of the user using **_Django Signals_**

**A. Documentation**

Please visit the <a href="https://auth-doc.algocode.site/doc/">documentation page</a>  for the detailed guide on Algocode Auth Service.

> However, all the APIs are referenced in the **_API Reference_** section below.

**B. Deployment**

> The service is deployed in Azure VM Ubuntu 22.04 server.

**C. About Algocode**

> This is Algocode Auth Service specific guideline.
>> **Please visit <a href="https://github.com/Mahboob-A/algocode">Algocode</a> to learn the mircroservices architecture of Algocode and more in-depth guideline how to submit a solution to Algocode platform.**

<br/> <br/><details>
<summary><h3 align="center">Development Stage</h3></summary>

#### Development Stage of Auth Service

The Algocode Auth Services uses the following services to serve the request during Development Stage.  

    a. Nginx as webserver.
    b. Gunicorn  as application server .
    c. Celery to process tasks asynchronously.
    d. Flower to monitor celery worker.
    e. Mailhog to mock email management.
    f. Django as backend.
    g. Django Rest Framework for API.
    h. PostgreSQL for user management database.
    i. Redis for celery backend. 
    l. Docker to containerize the service. 

<br/>
</details>

<details>
<summary><h3 align="center">Production Stage</h3></summary>

#### Production Stage of Auth Service

The Algocode Auth Services uses the following services to serve the request during Production Stage.  

    a. Nginx as webserver.
    b. Nginx Proxy Manager to manage Nginx.
    c. Portainer to manage and monitor docker container in Auth Service. 
    b. Gunicorn as application server.
    e. Celery to process tasks asynchronously.
    f. Flower to monitor celery worker.
    g. Resend as email service.
    h. Django as backend.
    i. Django Rest Framework for API.
    j. PostgreSQL for user management database.
    k. Redis for celery backend. 
    l. Docker to containerize the service. 

#### Deployment

The Auth Service is deployed in Azure VM Ubuntu 22.04 Server. 

<br/>
</details>

<details>
<summary><h3 align="center">Watch In Action</h3></summary>


#### A. Long Video (Describes all the features and architecture)
- Watch from `16:30` for code execution begin and  `18:30` for code submission result. 

<a href="https://www.youtube.com/watch?v=TbiRWL-11Fo&t=990s" target="_blank">
  <img src="https://img.youtube.com/vi/TbiRWL-11Fo/0.jpg" alt="Watch the video">
</a>

#### B. Short Video (Only core features) 
- Watch from `09:30` for code execution begin and  `11:30` for code submission result. 

<a href="https://www.youtube.com/watch?v=EgtAEjH53BA&t=571s" target="_blank">
  <img src="https://img.youtube.com/vi/EgtAEjH53BA/0.jpg" alt="Watch the video">
</a>
<br/>
</details>

<details>
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
</details>

<details>
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
</details>

<details>
<summary><h3 align="center">API Reference - Profile Details</h3></summary>


#### User Profile Details APIs

Profiles are the more user centric details for a user.

##### Get All User Profile Details 

```http
    GET  https://auth.algocode.site/api/v1/profile/all-user-profiles/
```

##### Get Profile Details of  an Authenticated User 

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

##### UPDATE Profile Details of an Authenticated User  

```http
     GET  https://auth.algocode.site/api/v1/profile/profile/update/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `gender`    | `string` |   `M`,  for  Male  `F` for Female , or `O` for Other. |
| `twitter_handle`    | `string` |   `Twitter` handle of the user. |
| `phone_number`    | `string` |  Phone number of the user.|

#### Healthcheck 

```http
     GET  https://auth.algocode.site/api/v1/common/healthcheck/
```

Please visit <a href="https://cm-doc.algocode.site/doc/">the documentation page</a>  for more details.

<br/>
</details>

<details>
<summary><h3 align="center">Run Locally and Contribution</h3></summary>

#### Run Locally

Please `fork` and `clone` this <a href="https://github.com/Mahboob-A/algocode-auth/tree/development/">development branch</a> of Algocode Auth Service, and follow along with the `envs-examples`. 

`cd` to `src` and create a `virtual environment`. Activate the virtual environment. 

Run `make docker-up` and the development setup will start running. Please install `make` in your host machine. 

If you use `Windows` Operating System, please run the  respective `docker commands` from the **`dev.yml`** docker compose file.

#### Contribution 

You are always welcome to contribute to the project. Please `open an issue` or `raise a PR` on the project.  

<br/>
</details>


<details>
  <summary><h3 align="center">Code Submission Result Examples</h3></summary>

<br/>

#### Some Code Submission Result Snapshots

<br/> 

##### A. AC Solution 

![dd8dbfe4-621b-49f1-b3a6-7ab2a892db87](https://github.com/Mahboob-A/algocode/assets/109282492/378d23ae-e059-47eb-866d-7c73d329b430) 
<br/>
<br/>

##### B. WA Solution 

![bedb4255-86c9-4417-b920-5976e6129cbb](https://github.com/Mahboob-A/algocode/assets/109282492/69bce2c1-5e16-4685-9069-23492068b55e)
<br/>
<br/>

##### C. Compilation Error

![1c5edd39-8ccd-4e23-a61d-66ae9564ca85](https://github.com/Mahboob-A/algocode/assets/109282492/9df40b17-b3f9-48d4-9662-3acdc1f594b8) 
<br/>
<br/>


##### D. Segmentation Fault 

![WhatsApp Image 2024-06-05 at 11 42 42 PM (1)](https://github.com/Mahboob-A/algocode/assets/109282492/0a3e1d3f-bafb-41a4-8f30-29eb5a9133e5)
<br/>
<br/>


##### E. Memory Limit Exceed

![WhatsApp Image 2024-06-05 at 11 42 03 PM (1)](https://github.com/Mahboob-A/algocode/assets/109282492/766f01f7-e97a-4aa7-858a-d7dddbf89b7d)
<br/>
<br/>


##### F. Time Limit Exceed 

![WhatsApp Image 2024-06-05 at 11 42 03 PM (1)](https://github.com/Mahboob-A/algocode/assets/109282492/766f01f7-e97a-4aa7-858a-d7dddbf89b7d)
<br/>
<br/>


</details>

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

[![Email Me](https://img.shields.io/badge/mahboob-black?style=flat&logo=gmail)](mailto:connect.mahboobalam@gmail.com?subject=Hello) 
  <a href="https://twitter.com/imahboob_a" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-05122A?style=flat&logo=twitter&logoColor=white" alt="Twitter">
  </a>
  <a href="https://linkedin.com/in/i-mahboob-alam" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-05122A?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://hashnode.com/@imehboob" target="_blank">
    <img src="https://img.shields.io/badge/Hashnode-05122A?style=flat&logo=hashnode&logoColor=white" alt="Hashnode">
  </a>
  <a href="https://medium.com/@imehboob" target="_blank">
    <img src="https://img.shields.io/badge/Medium-05122A?style=flat&logo=medium&logoColor=white" alt="Medium">
  </a>
  <a href="https://dev.to/imahboob_a" target="_blank">
    <img src="https://img.shields.io/badge/Dev.to-05122A?style=flat&logo=dev.to&logoColor=white" alt="Devto">
  </a>
  <a href="https://www.leetcode.com/mahboob-alam" target="_blank">
    <img src="https://img.shields.io/badge/LeetCode-05122A?style=flat&logo=leetcode&logoColor=white" alt="LeetCode">
  </a>
  
<br/>
<div align="center">
  <h3 align="center">Rest API with Flask & MongoDB</h3>
  <p align="center">
    <br />
    <a href="">View</a>
    ·
    <a href="https://github.com/leolupianez/restapi-flask-mongodb/issues">Report Bug</a>
    ·
    <a href="https://github.com/leolupianez/restapi-flask-mongodb/pulls">Request Feature</a>
    <br />
  </p>
</div>

## How It's Made:

A simple Rest API for updating a user in a MongoDB database. It includes endpoints for updating user details.

## Features

-   **Update user information**
-   **Authorization checks with session tokens**

## Tech Used:

[![Python][Python]][Python]
[![Flask][Flask]][Flask]
[![Pydantic][Pydantic]][Pydantic]

## Installation

```sh
pip install -r requirements.txt
```

### Things to add

-   Create a `.env` file in config folder and add the following as `key = value`
    -   MONGODB_URI = `Your MongoDB Connection String`

### Run

Start the development server

```sh
python main.py
```

## Authorization

The API uses bearer token authorization. To update the sample user include the following headers in your requests:

-   `Authorization: Bearer laurhln7t4gkhlnfsp7ywho_hlsfl`
-   `Session-Token: rbvkur79jksfu_shjhu`

## API Endpoints

### Update User

**Endpoint:** `/user`  
**Method:** `PUT`  
**Headers:**

-   `Authorization: Bearer laurhln7t4gkhlnfsp7ywho_hlsfl`
-   `Session-Token: rbvkur79jksfu_shjhu`
-   `Content-Type: application/json`

**Request Body:**

```json
{
    "user_id": "66b3d17ce6d8e2f5b93324d3",
    "first_name": "Test",
    "password": "Password",
    "updated_datetime": "2024-09-11T22:26:12.111Z"
}
```

<!-- MARKDOWN LINKS & IMAGES -->

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white
[Pydantic]: https://img.shields.io/static/v1?style=for-the-badge&message=Pydantic&color=E92063&logo=Pydantic&logoColor=FFFFFF&label=

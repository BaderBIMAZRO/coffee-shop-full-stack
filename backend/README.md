# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`

## Token
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpwWk1Xa29HSTFaU1NjOVdNWEJDaSJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktZnNuZC1jb2ZmZWUuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTE1MjEwMDg4NzE5NTI3MjczMzIyIiwiYXVkIjpbImRyaW5rcyIsImh0dHBzOi8vdWRhY2l0eS1mc25kLWNvZmZlZS5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTkzMTI5MDEzLCJleHAiOjE1OTMxMzYyMTMsImF6cCI6IjlTNWtKaVEyR2lxbHIyVG52elpvd3ZZTlVvRm1FS2JYIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsInBhdGNoOmRyaW5rcyIsInBvc3Q6ZHJpbmsiXX0.3Bf7LNnJbZDQLW3KH841WX5Y3kEzeDFM9rc3E-2REyo7_82lrolLnHSPgNrgIQj5gp2rH4Kq1HOBFClZFby7yykMKWZWkMgkPwEpiTA4kd6HaXLY4CbUphqu-kLvfSctLotOsJRKBCDdKoiOdl4sexbfGXo3kcX_Gdz1y9gXexQku3KVo0UqXGwQX4HYYxo6BPzoVibblnE9DpcCGaP3ljNUScoKTE5E0cu2arLDb8mE06ETWGoLaAYPj9qRZYMQJeoSQdU4JgcJ21iw4Dwn7i2lYCTjO_XF_Vvjbw4OdEVf6zxLGgBWaJN4hRNn9IVUpvibe3csyATVj8DqKtPmQg
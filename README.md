
# INSTALLATION

```bash
$ python3 -m venv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

# RUNNING

```bash
$ source ./env/bin/activate
$ flask run
$ open http://127.0.0.1:5000/
```

# ROUTES

	- /api/v1/register {'OPTIONS', 'POST'}
	- /api/v1/login {'OPTIONS', 'POST'}
	- /api/v1/user {'OPTIONS', 'POST'}
	- /api/v1/user/<string:public_id> {'GET', 'OPTIONS', 'HEAD'}
	- /api/v1/user/<string:public_id> {'PATCH', 'OPTIONS'}
	- /api/v1/user/<string:public_id> {'DELETE', 'OPTIONS'}
	- /static/<path:filename> {'GET', 'OPTIONS', 'HEAD'}
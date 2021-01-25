# Gunicorn

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.

## Dash

```py
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:8050 myapp:server
# remember to add app.server = server in the code, and change the binding to default
```

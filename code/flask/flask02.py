from hello import app
from flask import current_app
app_ctx = app.app_context()
app_ctx.push()
current_app.name
s=app_ctx.pop()
print(s)
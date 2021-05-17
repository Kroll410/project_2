from init import app
from init_models import init_db

init_db()
app.run(port='5000')

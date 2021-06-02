"""
Test development server run
"""

from init import app
from init_models import init_db

init_db()
# Run test server
# app.run(debug=True, port=8080)

import sys
import os

# Add the directory containing your module to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import your Flask application instance
from pet_finder import app as application

import sys, os

# CONFIGURE THIS
PROJECT = 'dizhayer.oscar.io'

# Run the venv interpreter
INTERP = os.path.join(os.environ['HOME'], PROJECT, 'venv', 'bin', 'python3')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

# Append full path to /app
sys.path.append(os.path.join(os.environ['HOME'], PROJECT, 'app'))

# Run application
from app.app import app as application

if __name__ == '__main__':
    application.run(debug=True)


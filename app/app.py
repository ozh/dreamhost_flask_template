from flask import Flask
import config

app = Flask(__name__)

# DISABLE DEBUG FOR PRODUCTION!
app.debug = True

@app.route('/')
def index():
    return 'it works'

if __name__ == '__main__':
    app.run()


import os
from dotenv import load_dotenv

load_dotenv()

from src import app


PORT = os.environ.get('PORT')
HOST = os.environ.get('HOST')
ENV = os.environ.get('ENV')
DEBUG = True if ENV != 'prd' else False

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)

from dotenv import load_dotenv
from flask import Flask
from routes import pages
import os
from pymongo import MongoClient


load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://sabari25:1998@cluster0.xfvmxcr.mongodb.net/current_app")
    app.db = client.get_default_database()

    app.register_blueprint(pages)
    return app
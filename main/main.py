"""The main module of the project to run it"""
from modules.visualization.app_flask import FLASK_APP


if __name__ == '__main__':
    FLASK_APP.run(port=4734)

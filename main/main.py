"""The main module of the project to run it"""
from modules.visualization.app_flask import FLASK_APP


# Enter your Twitter API keys in the file modules/twitter_list_adt/hidden.py
# before running the project
if __name__ == '__main__':
    FLASK_APP.run(port=4734)

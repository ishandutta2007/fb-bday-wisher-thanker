import os
import configparser
config = configparser.ConfigParser()
config.read("config.txt")

GOOG_ID = 'ishandutta2007'
GOOG_PASS = config.get("configuration", "goog_ishandutta2007_password")

FB_ID = 'ishandutta2007'
FB_PASS = config.get("configuration", "fb_ishandutta2007_password")

SCOPES = 'https://mail.google.com/'
APPLICATION_NAME = 'Gmail API Python Extract From Email'
CLIENT_SECRET_FILE = 'client_secret_ishandutta2007.json'# This file will be in local dir
CREDENTIAL_FILE_NAME = 'gmail-python-email-list_ishandutta2007.json'

CHROME_DRIVER_PATH = '/Users/ishandutta2007/Documents/Projects/chromium/chromium/src/out/Default/chromedriver_gleam'

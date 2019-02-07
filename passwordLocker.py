import argparse
import requests
from user import user

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Enter name")
parser.add_argument("password", help="Enter password")
args = parser.parse_args()
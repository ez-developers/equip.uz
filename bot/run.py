import sys
import os
import io
from main import main
from dotenv import load_dotenv, find_dotenv, dotenv_values

load_dotenv()
token = os.getenv('API_TOKEN')
print(token)

if __name__ == '__main__':
    if token is None:
        t = input("Good! Paste the API token:\n")
        os.putenv("API_TOKEN", t)
        print("Successfully set API TOKEN!")
    else:
        print("Current api token is: " + str(token))

import sys
import os
import io
from main import main
from dotenv import load_dotenv, find_dotenv, dotenv_values

load_dotenv()
token = os.getenv('API_TOKEN')
bot_name = None

if __name__ == '__main__':
    main()
    # if token is None:
    #     t = input("Good! Paste the API token:\n>>>")
    #     os.putenv("API_TOKEN", t)
    #     print("Successfully set API TOKEN!")
    # else:
    #     print("Current API token is: " + str(token))
    #     print(f"Bot is: {bot_name}")
    #     input("Would you like to change it? [y/n]: ")

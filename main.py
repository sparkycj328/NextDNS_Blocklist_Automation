import os

from dotenv import load_dotenv


def main():
    # load .env file to environment
    load_dotenv()

    API = os.getenv("API")
    print(API)


if __name__ == "__main__":
    main()

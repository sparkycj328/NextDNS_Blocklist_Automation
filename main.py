import os
import sys

import requests
from dotenv import load_dotenv


def main():
    # ensure proper command line variables were passed
    if len(sys.argv) != 2:
        print("(+) Usage: %s (True || False)" % sys.argv[0])
        print("(+) Example: %s True" % sys.argv[0])
        sys.exit(-1)

    # access the .env variables and add CLI variable
    configuration = load_environment()
    configuration.update({"active": sys.argv[1]})
    make_request(configuration)


# load_environment variables from the .env file
def load_environment():
    # load .env file to environment
    load_dotenv()

    # create a dict to store the variables
    configuration = dict(
        api=os.getenv("API"),
        profile_id=os.getenv("PROFILE"),
        deny_domain=os.getenv("DENYURL").encode().hex(),
    )
    return configuration


# make_request is responsible for creating and sending the HTTP PATCH request as the domain already exists
def make_request(configuration):
    deny_endpoint = f"https://api.nextdns.io/profiles/{configuration['profile_id']}/denylist/hex:{configuration['deny_domain']}"

    # convert the active field into a boolean
    if configuration["active"].lower() == "true":
        configuration["active"] = True
    else:
        configuration["active"] = False

    response = requests.patch(
        url=deny_endpoint,
        json={"active": configuration["active"]},
        headers={"X-Api-Key": configuration["api"]},
    )

    if response.status_code not in [200, 204]:
        print(response.status_code, response.content)

    return


if __name__ == "__main__":
    main()

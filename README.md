# Instructions to Run

There are two primary ways of running this script.

## Common steps for both methods
Create a .env file in the same directory. The .env file should have the following fields
    - API=YOUR_API_KEY
    - PROFILE=YOUR_PROFILE_ID  (This can be located within NextDNS)
    - DENYURL=URL_TO_BE_ENABLED_OR_DENIED (This URL should already be added for the sake of this script)

## Using UV
1. Clone project
2. Run the 'uv sync' command to install the python version, create a virtual environment, and install dependencies
3. Run the script via 'uv run main.py True' or 'uv run main.py False' 

## Using pip
1. Clone project
2. Ensure you have python and pip installed
3. pip install -r requirements.txt
4. Run either of the following commands: 'python main.py True' or 'python main.py False'
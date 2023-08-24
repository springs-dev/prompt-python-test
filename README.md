# Decision Making Process Formatter

This project allows you to format a given text describing a decision-making process into a structured table format. The resulting table will be saved in a CSV file.

## Getting Started

Follow these steps to set up and run the project:

### Clone the Repository

Clone the repository from GitLab:

```shell
git clone https://github.com/springs-dev/prompt-python-test.git
cd decision-making-process-formatter
```
### Set Up Virtual Environment
Create and activate a virtual environment:

```shell
python3 -m venv venv
source venv/bin/activate # on Windows venv\Scripts\activate
```

### Install Dependencies
Install the required Python packages:
```shell
pip install -r requirements.txt
```
### Configure OpenAI API Key
Copy the provided OpenAI API key and create a .env file like .env.sample in the project directory. Paste the key into the .env file:
### Run app
```shell
python api.py
```
### Customize Input Text
In the context of using the API endpoint, you can send a POST request with a JSON payload containing the input_text to the /split-text endpoint. The API will process the input text, format it, and save the result in a CSV file.

The resulting table will be saved in the actions.csv file.

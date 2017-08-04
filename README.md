# TemperatureChart
To run this
First, You need to have matplotlib and google API library:
pip install --upgrade google-api-python-client
pip install matplotlib

Then, put python file and json file into Python main directory
Second, python getData.py
Then, you will be asked to logon your google account
You will see my temperature chart from the sheet:
https://docs.google.com/spreadsheets/d/1_4Nz2WlAWQlpK8j3XaMYXPCJ6E427E9WdmiGLfbuleQ/edit#gid=0

Working principle:
1. Get Credential for Google API
2. Get values from Spreadsheet
3. Process values to format of datetime and float
4. time consistency checking 
5. plot the temperature data

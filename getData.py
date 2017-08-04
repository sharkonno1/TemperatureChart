#from __future__ import print_function
from datetime import datetime
import matplotlib.pyplot as plt
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'plotData'


def get_credentials():
    """Gets valid user credentials from storage.
        
        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
        
        Returns:
        Credentials, the obtained credential.
        """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')
    store = Storage(credential_path)
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    if flags:
        credentials = tools.run_flow(flow, store, flags)
    else: # Needed only for compatibility with Python 2.6
        credentials = tools.run(flow, store)
    #print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.
        
        Creates a Sheets API service object and prints the names and majors of
        students in a sample spreadsheet:
        https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
        """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                                              discoveryServiceUrl=discoveryUrl)
                    
    spreadsheetId = '1_4Nz2WlAWQlpK8j3XaMYXPCJ6E427E9WdmiGLfbuleQ'
    rangeName = 'Sheet1!A2:B'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    #if not values:
    #print('No data found.')
    #else:
    #print('Name, Major:')
    temps=[]
    times=[]
    for row in values:
        temp = float(row[1])
        temps.append(temp)
        time = datetime.strptime(row[0],'%m/%d/%Y %H:%M:%S')
        times.append(time)
    t1 = []
    t2 = []
    T1 = []
    T2 = []
    ref = times[0].day
    i = 0
    for time in times:
        if time.day == ref:
            t1.append(time)
            T1.append(temps[i])
        else:
            t2.append(time)
            T2.append(temps[i])
        i = i + 1

    plt.plot_date(t2,T2)
    plt.ylabel('Temperature')
    plt.xlabel('time')
    plt.show()
if __name__ == '__main__':
    main()

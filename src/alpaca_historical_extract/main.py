# standard libraries

import datetime as dt

# non-standard libraries

# internal libraries
import core_library
import extract_library
import hub
import api_library
import dbmsIO

# global variables
scriptStart = ''

if __name__ == '__main__':
    loginSuccessful, api, credentials = hub.init()
    # print(loginSuccessful,api,credentials)

    if loginSuccessful:
        # print(api.get_account())

        hub.update_dbs(credentials, api, tckrs='', modeling=False, forceFDataPull=False,
                       forceMDataPull=True, verbose=True)
        keys = hub.get_datasets()
        #print(keys)
        dataset = hub.get_table(dataset=keys, raw=True)
        #for key, value in dataset.items():
            #print(key)
            #print(value['STAT DATA'].to_string())
        #print(dataset['DAILY MARKET DATA'])
        # data = hub.get_table(keys[0],True)
        # print(data)
    # ttr = str(dt.timedelta(seconds=(dt.datetime.now() - scriptStart).seconds))
    # print("script time to run:", ttr)
    # core_library.log_entry(logFile="project_log.txt", logText=("script time to run: ", ttr), logMode='a')

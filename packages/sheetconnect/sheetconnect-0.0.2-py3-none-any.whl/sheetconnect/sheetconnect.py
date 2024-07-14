import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

class Connect:
    def GetDF_Sheet(credential, sheet, sheet_name):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credential, scope)
        gc = gspread.authorize(credentials)
        sh = gc.open(sheet)
        df_sheet = sh.worksheet(sheet_name)
        df = pd.DataFrame(df_sheet.get_all_records())
        return df
# previously used code



# import os
# import gspread
# from google.oauth2.service_account import Credentials

# def is_access_granted(email, key):
#     # Define the scope and authorize the credentials
#     scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    
#     # Get the path to the credentials.json file
#     creds_path = os.path.join(os.path.dirname(__file__), 'credentials.json')
#     creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
#     client = gspread.authorize(creds)

#     # Open the Google Sheet using the sheet ID
#     sheet_id = "1T2GQT5l_OhSR2g2ZkuOUHLcpK7MeXdRov50ETnmOCn4"
#     sheet = client.open_by_key(sheet_id)

#     # Get all records from the Google Sheet
#     records = sheet.sheet1.get_all_records()

#     # Verify email and key
#     for record in records:
#         if record['email'] == email and record['keys'] == key and record['Status'] == "Active":
#             return True
#     return False

# easyRTML/check.py
import os
import gspread
from google.oauth2.service_account import Credentials
from cryptography.fernet import Fernet

def load_credentials():
    # Load the secret key
    with open(os.path.join(os.path.dirname(__file__), 'secret.key'), 'rb') as key_file:
        key = key_file.read()
    cipher_suite = Fernet(key)

    # Load and decrypt the credentials
    encrypted_path = os.path.join(os.path.dirname(__file__), 'credentials.encrypted')
    with open(encrypted_path, 'rb') as encrypted_file:
        encrypted_credentials = encrypted_file.read()
    decrypted_credentials = cipher_suite.decrypt(encrypted_credentials)

    return decrypted_credentials

def is_access_granted(email, key):
    # Define the scope and authorize the credentials
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    
    # Load and decrypt the credentials
    decrypted_credentials = load_credentials()
    creds = Credentials.from_service_account_info(eval(decrypted_credentials.decode()), scopes=scopes)
    client = gspread.authorize(creds)

    # Open the Google Sheet using the sheet ID
    sheet_id = "1T2GQT5l_OhSR2g2ZkuOUHLcpK7MeXdRov50ETnmOCn4"
    sheet = client.open_by_key(sheet_id)

    # Get all records from the Google Sheet
    records = sheet.sheet1.get_all_records()

    # Verify email and key
    for record in records:
        if record['email'] == email and record['keys'] == key and record['Status'] == "Active":
            return True
    return False

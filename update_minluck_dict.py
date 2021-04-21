import gspread
from mouse import Mouse
import pickle

GOOGLE_SHEET_KEY = '13hKjNDFTFR3rTkmQzyi3d4ZDOlQJUvTfWPDQemmFW_Y'
CREDENTIALS_FILENAME = 'credentials.json'

worksheet = gspread.service_account(filename=CREDENTIALS_FILENAME).open_by_key(GOOGLE_SHEET_KEY).sheet1.get_all_values()[1:]
print("Worksheet loaded")

mouse_minlucks = {}

for breed in worksheet:
    values = list(map(lambda x: None if x == '∞' or x == '' else x, breed))
    mouse_minlucks[values[0].lower()] = Mouse(values[0], values[1], values[3], values[4:], values[2])
    # Name, Group, Power, Minlucks by Powertype (list), Subgroup
print("Dictionary populated")

filehandler = open('minluck_dict', 'w+b')
pickle.dump(mouse_minlucks, filehandler)
filehandler.close()
print("Dictionary Pickled")

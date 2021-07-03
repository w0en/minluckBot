import gspread
from mouse import Mouse
import pickle

# Constants
GOOGLE_SHEET_KEY = '13hKjNDFTFR3rTkmQzyi3d4ZDOlQJUvTfWPDQemmFW_Y'
CREDENTIALS_FILENAME = 'credentials.json'

# Loading the data
worksheet = gspread.service_account(filename=CREDENTIALS_FILENAME).open_by_key(GOOGLE_SHEET_KEY).sheet1.get_all_values()[1:]
print("Worksheet loaded")

# Populating Dictionary
# Dictionary contains breeds as key and instances of the Mouse class as values
mouse_minlucks = {}

print("Populating Dictionary")
for entry in worksheet:
    values = list(map(lambda x: None if x == '∞' or x == '' else x, entry))
    mouse_minlucks[values[0].lower()] = Mouse(breed=values[0],
                                              group=values[1],
                                              power=values[3],
                                              minlucks=values[4:],
                                              subgroup=values[2])
    # Name, Group, Power, Minlucks by Powertype (list), Subgroup
print("Dictionary populated")

# Saving the data
with open('minluck_dict2', 'w+b') as filehandler:
    pickle.dump(mouse_minlucks, filehandler)
print("Dictionary Pickled")

# Testing
# print(mouse_minlucks["nachous, the molten"])

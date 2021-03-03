import pickle

# Base Dictionary

filehandler = open('base_dict', 'wb')
base_dict = pickle.load(filehandler)
filehandler.close()
print("Base Dictionary Loaded")

# Mouse Groups Dictionary
mouse_groups = {}

# Mouse Subgroups Dictionary
mouse_subgroups = {}

# Mouse Custom Groups Dictionary
mouse_custom_groups = {}

# Mouse Area Dictionary
mouse_areas_dictionary = {}

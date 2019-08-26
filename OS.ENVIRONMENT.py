# https://www.programcreek.com/python/example/10/os.environ
# https://www.geeksforgeeks.org/python-os-environ-object/

import os
import pprint
# Get the list of user's environment variables
envr_var = os.environ 
# Print the list of user's environment variables
print("User's Environment variables: ")
print(dict(envr_var))
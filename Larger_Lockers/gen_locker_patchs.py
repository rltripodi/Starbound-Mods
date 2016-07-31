# Changes ship and storage locker slots to equal arg1 and arg2 respectively (<= 256).
# Check the /interfaces/chest folder for the slot numbers supported by the corresponding .config files

import sys

RACES = ["apex", "avian", "floran", "glitch", "human", "hylotl", "novakid"]

if len(sys.argv) != 3:
	print("Usage:\n\tgen_locker_patchs.py <shiplocker slots> <storagelocker slots>")
else:
	for ii in range(len(RACES)):
		shiplocker = open("objects/ship/" + RACES[ii] + "shiplocker/" + RACES[ii] + "shiplocker.object.patch", "w")
		shiplocker.write('[\n\t{ "op": "replace", "path": "/slotCount", "value": ' + sys.argv[1] + ' }\n]')
		shiplocker.close()
		
		storagelocker = open("objects/" + RACES[ii] + "/" + RACES[ii] + "storagelocker/" + RACES[ii] + "storagelocker.object.patch", "w")
		storagelocker.write('[\n\t{ "op" : "replace", "path" : "/slotCount", "value" : ' + sys.argv[2] + ' }\n]')
		storagelocker.close()
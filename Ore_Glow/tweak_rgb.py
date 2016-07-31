import glob, os
os.chdir("./")
for file in glob.glob("*.matmod.patch"):
	f = open(file, 'w')
	f.write('[\n\t{\n\t\t"op": "add",\n\t\t"path": "/renderParameters/radiantLight",\n\t\t"value": [20, 20, 20]"\n\t}\n]')
	f.close()
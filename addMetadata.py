import os
import csv
import xml.etree.ElementTree as ET
ET.register_namespace("", "http://www.loc.gov/mods/v3")
ns = {"mods":"{http://www.loc.gov/mods/v3"}


metadict = {}
data = csv.reader(open("maps.csv", "r"))
for rows in data:
    druid = rows[0]
    call_num = rows[6]
    sequence = rows[7]
    metadict[druid] = call_num, sequence


def getText(druid, pn, note):
    for k, v in metadict.items():
        if k == druid:
            pn.text = v[0]
            note.text = v[1]
    

def addElements():
    pn = ET.Element("{http://www.loc.gov/mods/v3}partName")
    note = ET.Element("{http://www.loc.gov/mods/v3}note")
    note.set("type","date/sequential designation")
    titleInfo.insert(1,pn)
    root.insert(n_index, note)
    getText(druid, pn, note)
    print (f, pn.text, note.text)
        

for dirName, subDirs, fileNames in os.walk('.'):
    for f in fileNames:
        if f.startswith ("druid") and f.endswith(".xml"):
            druid = f[6:-4]
            filePath = os.path.join(dirName, f)
            tree = ET.parse(filePath)
            root = tree.getroot()
            titleInfo = root.find("{http://www.loc.gov/mods/v3}titleInfo", ns)
            last_note = root.findall("{http://www.loc.gov/mods/v3}note", ns)[-1]
            n_index = root.getchildren().index(last_note)
            n_index = n_index + 1
            druid = f[6:-4]
            addMeta = addElements()
            tree.write(filePath)
            
            

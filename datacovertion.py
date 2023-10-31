#Question 8:-Once You have printed the above result.
#a. now convert the lists above into comma seperated values (Type Tags and Names)
#    For Example - executable, windows, win32,  pe, pedll
#b. Convert Last modification date into human readable format (epoch into datetime)
#              



import json
from datetime import datetime

# The provided JSON response
json_data = '''
{
   "data":{
      "attributes":{
         "type_description":"Win32 DLL",
         "type_tags":[
            "executable",
            "windows",
            "win32",
            "pe",
            "pedll"
         ],
         "names":[
            "d196dee3ea38475845b79232b0732084",
            "d4f49b363cab452602260c2c658df12b36d27279.bin",
            "ldss9PQPC.xlsm",
            "I0znS.msc"
         ],
         "last_modification_date":1657137577
      }
   }
}
'''

# Load the JSON data
parsed_data = json.loads(json_data)

# Extract the attributes
type_description = parsed_data['data']['attributes']['type_description']
type_tags = parsed_data['data']['attributes']['type_tags']
names = parsed_data['data']['attributes']['names']
last_modification_date = parsed_data['data']['attributes']['last_modification_date']

# Convert lists to comma-separated values
type_tags_csv = ', '.join(type_tags)
names_csv = ', '.join(names)

# Convert epoch time to human-readable format
last_modification_date_readable = datetime.utcfromtimestamp(last_modification_date).strftime('%Y-%m-%d %H:%M:%S')

# Print the results
print("Type Description:", type_description)
print("Type Tags (CSV):", type_tags_csv)
print("Names (CSV):", names_csv)
print("Last Modification Date (Readable):", last_modification_date_readable)

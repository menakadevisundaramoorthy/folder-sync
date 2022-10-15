import os
import webbrowser
from file_utils import *
import json 


data = read_csv("folder_sync_metrics.csv")
table_data = str(json.dumps(data, indent = 4))
sync_number = get_values_from_dict(data, 'sync_number')
sync_time = get_values_from_dict(data, 'sync_time')

print(str(table_data))

index = open("folder_sync_metrics.html").read().rstrip("\n").format(sync_number=sync_number, 
                                         sync_time=sync_time,
                                         table_data=table_data)

html = '<html> {} </html>'.format(index)
path = os.path.abspath('temp.html')
url = 'file://' + path

with open(path, 'w') as f:
    f.write(html)
webbrowser.open(url)

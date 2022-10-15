import os
import csv

# Create a new folder
def create_folder(path):
  if not path:
    return 'WARNING - Path cannot be empty.'
  if not os.path.isdir(path):
    os.makedirs(path)
    return "Created a new folder - " + path
  else:
    return "WARNING - The folder " + path + " already exists."


# Create a new file or Update the existing file
def create_or_update_file(file_name, file_content, is_update):
  if not file_name:
    return 'WARNING - File name cannot be empty.'
  try:
    message = ""
    if not is_update:
      with open(file_name, 'w') as writeFile:
        writeFile.write(file_content)
        message = 'Created a new file - {}'.format(file_name)
    else: 
      with open(file_name, 'a') as updateFile:
        updateFile.write(file_content)
        message = 'Updated the file - {}'.format(file_name)
    return message
  except Exception as exception:
    return 'EXCEPTION - Exception in file_utils.create_or_update_file - ' + str(exception)


# To check if a folder exists in a given path or not
def is_folder_exists(path):
  return os.path.isdir(path)


# deletes the file if present else returns the message file does not exists
def delete_file(file_path):
  if not file_path:
    return 'WARNING - File path cannot be empty.'
  if os.path.isfile(file_path):
    os.remove(file_path)
    return('Deleted the file - {}'.format(file_path))
  else:
    return 'WARNING - {} does not exist'.format(file_path)


# Delete the existing folder
def delete_folder(folder_path):  
  if not folder_path:
    return 'WARNING - Folder path cannot be empty.'
  if not os.listdir(folder_path):
    os.rmdir(folder_path)
    return "Deleted the folder " + folder_path
  else:
    return "EXCEPTION - The folder " + folder_path + " is not empty."


# Read a file path
def read_file(file_path):
  if not file_path:
    return 'File path cannot be empty.'
  try:
    with open(file_path) as readfile:
      lines = readfile.readlines()
      return 'Read the file - {}'.format(file_path)
  except Exception as exception:
    return 'Exception in file_utils.read_file - ' + str(exception)


# Create a new folder
def create_folder_in_path(path, folder_name):
  folder = path + '/' + folder_name
  if not path or not folder_name:
    return 'Path or Folder name cannot be empty.'
  try:
    # Create target Folder
    os.makedirs(folder)
    return "Created a new folder - " + folder
  except FileExistsError:
    return 'Exception in file_utils.create_folder - ' + folder + " already exists."


def file_is_hidden(p):
  if os.name == 'nt':
    attribute = win32api.GetFileAttributes(p)
    return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
  else:
    return p.startswith('.') #linux-osx


# Metrics Utils


def capture_metrics(sync_time):
  last_sync_number = 0
  csv_data = read_csv('meta/folder_sync_metrics.csv')
  if csv_data:
    last_sync_number = int(csv_data[-1]['sync_number'])
  with open('meta/folder_sync_metrics.csv', 'a', newline='') as csvfile:
    fieldnames = ['sync_number', 'sync_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'sync_number': last_sync_number + 1, 'sync_time': float(sync_time)})


def create_metrics_file():
  with open('meta/folder_sync_metrics.csv', 'w', newline='') as csvfile:
    fieldnames = ['sync_number', 'sync_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


def read_csv(file_path):
  with open(file_path, 'r') as f:
    csv_reader = csv.reader(f)
    result = []
    for sync_number,sync_time in csv_reader:
      if not sync_number == 'sync_number':
        result.append(dict({'sync_number': int(sync_number), 'sync_time': float(sync_time)}))
    return result

def get_values_from_csv(csv_file, field_name):
  result = read_csv(csv_file)
  return [d[field_name] for d in result if field_name in d]

def get_values_from_dict(input_dict, field_name):
  return [d[field_name] for d in input_dict if field_name in d]
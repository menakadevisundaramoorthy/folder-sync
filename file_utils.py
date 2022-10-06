# Create a new file or Update the existing file
def create_or_update_file(file_name, file_content, is_update):
  if not file_name:
    return 'File name cannot be empty.'
  try:
    with open(file_name, 'a' if is_update else 'w') as writefile:
      writefile.write(file_content)
      message = 'Updated the file - {}'.format(file_name) if is_update else 'Created a new file - {}'.format(file_name)
      print(message)
      return message
  except Exception as exception:
    print(exception)
    return exception


# Read a file path and print the file content
def read_file(file_path):
  if not file_path:
    return 'File path cannot be empty.'
  try:
    with open(file_path) as readfile:
      lines = readfile.readlines()
      print('Read the file - {} and the content is:'.format(file_path))
      print(lines)
      return 'Read the file - {}'.format(file_path)
  except Exception as exception:
    print(exception)
    return exception


# deletes the file if present else prints the message file does not exists
def delete_file(file_path):
  if not file_path:
    return 'File path cannot be empty.'
  import os
  if os.path.isfile(file_path):
    os.remove(file_path)
    message = 'Deleted the file - {}'.format(file_path)
    print(message)
    return(message)
  else:
    message = '{} does not exist'.format(file_path)
    print(message)
    return message


# Create a new folder
def create_folder(path, folder_name):
  folder = path + '/' + folder_name
  if not path or not folder_name:
    return 'Path or Folder name cannot be empty.'
  try:
    # Create target Folder
    import os
    os.mkdir(folder)
    message = "Folder " + folder + " created."
    print(message)
    return message 
  except FileExistsError:
    message = "Folder " + folder + " already exists."
    print(message)
    return message


# Delete the existing folder
def delete_folder(folder_path):  
  if not folder_path:
    return 'Folder path cannot be empty.'
  import os
  if not os.listdir(folder_path):
    os.rmdir(folder_path)
    message = "Folder " + folder_path + " deleted."
    print(message)
    return message 
  else:
    message = "Folder " + folder_path + " is not empty."
    print(message)
    return message
  
import pytest
from file_utils import *

def test_create_or_update_file():
  assert create_or_update_file('folder_test/write_file.txt', 'Hello, This is a create file.', False) == "EXCEPTION - Exception in file_utils.create_or_update_file - [Errno 2] No such file or directory: 'folder_test/write_file.txt'"
  assert create_or_update_file('write_file.txt', 'Hello, This is a create file.', False) == 'Created a new file - write_file.txt'
  assert create_or_update_file('', 'Hello, This is a create file.', False) == 'WARNING - File name cannot be empty.'
  assert create_or_update_file('write_file.txt', 'Hello, This is a update file.', True) == 'Updated the file - write_file.txt'


def test_read_file():
  assert read_file('folder_test/read_file.txt') == "Exception in file_utils.read_file - [Errno 2] No such file or directory: 'folder_test/read_file.txt'"
  assert read_file('write_file.txt') == 'Read the file - write_file.txt'
  assert read_file('') == 'File path cannot be empty.'


def test_delete_file():
  assert delete_file('folder_test/delete_file.txt') == 'WARNING - folder_test/delete_file.txt does not exist'
  assert delete_file('write_file.txt') == 'Deleted the file - write_file.txt'
  assert delete_file('') == 'WARNING - File path cannot be empty.'
  

def test_create_folder_in_path():
  assert create_folder_in_path('', '') == 'Path or Folder name cannot be empty.'
  assert create_folder_in_path('', 'test_folder_name') == 'Path or Folder name cannot be empty.'
  assert create_folder_in_path('test_path', '') == 'Path or Folder name cannot be empty.'
  assert create_folder_in_path('..', 'folder-sync') == 'Exception in file_utils.create_folder - ../folder-sync already exists.'
  assert create_folder_in_path('.', 'empty_folder') == 'Created a new folder - ./empty_folder'
  assert create_folder_in_path('.', 'folder_with_file') == 'Created a new folder - ./folder_with_file'
  assert create_or_update_file('folder_with_file/write_file.txt', 'Hello, This is a create file.', False) == 'Created a new file - folder_with_file/write_file.txt'


def test_delete_folder():
  assert delete_folder('') == 'WARNING - Folder path cannot be empty.'
  assert delete_folder('empty_folder') == 'Deleted the folder empty_folder'
  assert delete_folder('folder_with_file') == 'EXCEPTION - The folder folder_with_file is not empty.'
  assert delete_file('folder_with_file/write_file.txt') == 'Deleted the file - folder_with_file/write_file.txt'
  assert delete_folder('folder_with_file') == 'Deleted the folder folder_with_file'


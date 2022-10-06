import pytest
from file_utils import *

def test_create_or_update_file():
  assert str(create_or_update_file('folder_test/write_file.txt', 'Hello, This is a create file.', False)) == str(FileNotFoundError(2, 'No such file or directory: \'folder_test/write_file.txt\''))
  assert create_or_update_file('write_file.txt', 'Hello, This is a create file.', False) == 'Created a new file - write_file.txt'
  assert create_or_update_file('', 'Hello, This is a create file.', False) == 'File name cannot be empty.'
  assert create_or_update_file('write_file.txt', 'Hello, This is a update file.', True) == 'Updated the file - write_file.txt'


def test_read_file():
  assert str(read_file('folder_test/read_file.txt')) == str(FileNotFoundError(2, 'No such file or directory: \'folder_test/read_file.txt\''))
  assert read_file('write_file.txt') == 'Read the file - write_file.txt'
  assert read_file('') == 'File path cannot be empty.'


def test_delete_file():
  assert delete_file('folder_test/delete_file.txt') == 'folder_test/delete_file.txt does not exist'
  assert delete_file('write_file.txt') == 'Deleted the file - write_file.txt'
  assert delete_file('') == 'File path cannot be empty.'


def test_create_folder():
  assert create_folder('', '') == 'Path or Folder name cannot be empty.'
  assert create_folder('', 'test_folder_name') == 'Path or Folder name cannot be empty.'
  assert create_folder('test_path', '') == 'Path or Folder name cannot be empty.'
  assert create_folder('..', 'folder-sync') == 'Folder ../folder-sync already exists.'
  assert create_folder('.', 'empty_folder') == 'Folder ./empty_folder created.'
  assert create_folder('.', 'folder_with_file') == 'Folder ./folder_with_file created.'
  assert create_or_update_file('folder_with_file/write_file.txt', 'Hello, This is a create file.', False) == 'Created a new file - folder_with_file/write_file.txt'


def test_delete_folder():
  assert delete_folder('') == 'Folder path cannot be empty.'
  assert delete_folder('empty_folder') == 'Folder empty_folder deleted.'
  assert delete_folder('folder_with_file') == 'Folder folder_with_file is not empty.'
  assert delete_file('folder_with_file/write_file.txt') == 'Deleted the file - folder_with_file/write_file.txt'
  assert delete_folder('folder_with_file') == 'Folder folder_with_file deleted.'
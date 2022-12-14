import sys,logging,os, threading
from datetime import datetime
from file_utils import *
from pathlib import Path


SOURCE_FOLDER = sys.argv[1]
LOG_FILE = sys.argv[2]
SYNC_INTERVAL_IN_SECONDS = int(sys.argv[3])
LAST_SYNC_TIME = float(0)
TARGET_FOLDER = SOURCE_FOLDER + "_replica"

if os.name == 'nt':
  import win32api, win32con


logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
if not os.path.exists('meta/folder_sync_metrics.csv'):
  create_metrics_file()

def perform_sync():

  # validate source folder
  if is_folder_exists(SOURCE_FOLDER):
    if not is_folder_exists(TARGET_FOLDER):
      log_and_print('The folder ' + TARGET_FOLDER + ' does not exists.')
      create_folder(TARGET_FOLDER)
  else:
    log_and_print('Error: The source folder {} does not exists. Please provide a valid source folder.'.format(SOURCE_FOLDER))
    exit()


  #############################################################
  ############      Prep work for every sync       ############
  #############################################################
  print('###################################### FOLDER SYNC - BEGIN ######################################')
  start_time = datetime.now()
  log_and_print('Folder sync started at ' + start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
  global LAST_SYNC_TIME
  if not LAST_SYNC_TIME:
    log_and_print('Synchronizing all the files and folders from the path {}'.format(SOURCE_FOLDER))
  else:
    log_and_print('Synchronizing the files and folders created/modified/removed after the last sync completed time ' + datetime.fromtimestamp(LAST_SYNC_TIME).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + ' from the path ' + SOURCE_FOLDER)


  #############################################################
  ############   Create/Modify files and Folders   ############
  #############################################################
  # BEGIN to create or modify new/existing source file/folder to target file/folder
  source_data_set = set(sorted(Path(SOURCE_FOLDER).rglob("*"), key =lambda directory_element: os.path.getmtime(directory_element)))
  new_target_data_set = set()
  for source_data in source_data_set:
    target_data = os.path.abspath(source_data).replace(SOURCE_FOLDER, TARGET_FOLDER)
    new_target_data_set.add(target_data)

    # logic to verify the last sync time and perform sync only on the delta changes
    if (float(os.path.getmtime(source_data)) > LAST_SYNC_TIME) or (float(os.path.getctime(source_data)) > LAST_SYNC_TIME):
      create_file_or_folder(source_data, target_data, float(LAST_SYNC_TIME) > float(0))
  # END to create or modify new/existing source file/folder to target file/folder


  #############################################################
  ############     Remove files and Folders        ############
  #############################################################
  # BEGIN delete source file/folder to target file/folder
  target_data_set = set(sorted(Path(TARGET_FOLDER).rglob("*"), key =lambda directory_element: os.path.getmtime(directory_element)))
  created_targets = set()
  for i in target_data_set:
    created_targets.add(os.path.abspath(i))
  delete_data_set = created_targets - new_target_data_set
  for delete_data in delete_data_set:
    if os.path.isdir(delete_data):
      log_and_print(delete_folder(str(delete_data)))
    else:
      log_and_print(delete_file(str(delete_data)))
  # END delete source file/folder to target file/folder


  #############################################################
  ############   Work after every sync completion  ############
  #############################################################
  end_time = datetime.now()
  LAST_SYNC_TIME = datetime.timestamp(end_time)
  log_and_print("Folder sync completed at " + end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
  sync_time = datetime.timestamp(end_time) - datetime.timestamp(start_time)
  capture_metrics(sync_time)
  print('###################################### FOLDER SYNC - END   ######################################\n')


def create_file_or_folder(source_data, target_data, is_delta_sync):
  if os.path.isdir(source_data):
    if not is_folder_exists(target_data):
      log_and_print(create_folder(target_data))
      if is_delta_sync:
        new_folder_data = set(sorted(Path(source_data).rglob("*"), key =lambda directory_element: os.path.getmtime(directory_element)))
        for folder_data in new_folder_data:
          new_target_data = os.path.abspath(folder_data).replace(SOURCE_FOLDER, TARGET_FOLDER);
          create_file_or_folder(folder_data, new_target_data, is_delta_sync)
  else:
    if not file_is_hidden(os.path.basename(source_data)):
      folder_path_from_file = os.path.abspath(target_data).replace('/' + os.path.basename(target_data), '')
      if not is_folder_exists(folder_path_from_file):
        log_and_print(create_folder(folder_path_from_file))
      if os.path.exists(target_data):
        log_and_print(delete_file(target_data))
      with open(source_data) as read_file: content = read_file.read()
      log_and_print(create_or_update_file(target_data, content, False))


def log_and_print(message):
  print(message)
  if (message.startswith('WARNING - ')):
    logging.warning(message.replace('WARNING - ', ''))
  elif(message.startswith('EXCEPTION')):
    logging.exception(message.replace('EXCEPTION - ', ''))
  else:
    logging.info(message)


ticker = threading.Event()
perform_sync()
while not ticker.wait(SYNC_INTERVAL_IN_SECONDS):
  perform_sync()
    
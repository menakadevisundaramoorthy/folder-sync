
# folder-sync
One-way periodic folder synchronization between source and replica folder

## Table of contents

- [Pre requisite](#pre-requisites)
- [How to use folder sync?](#how-to-use-folder-sync?)
- [Test Cases](#test-cases)
- [Documentation](#documentation)
- [Metrics](#metrics)

## Pre-requisite
Install `python` or `python3`, additionally, install `pytest` to execute and verify the test cases.

## How to use folder-sync?
The folder-sync operates in command line and it takes three command line arguments, those are

 1. Source folder - for which the replica has to be created
 2. Log file - all the folder sync operations are tracked and logged
 3. Sync interval - the periodic interval of which the folder sync operation need to be done

### Steps to run folder sync
**Step-1:**
    `git clone https://github.com/menakadevisundaramoorthy/folder-sync.git`

**Step-2:**
    `cd folder-sync`

**Step-3:**
    `python folder-sync.py [PATH_TO_SOURCE_FOLDER] [PATH_TO_LOG_FILE] [SYNC_INTERVAL_IN_SECONDS]`

If the log file is not available, in the location, then it creates one. If the source folder is not available in the specified location, folder-sync throws error and synchronization does not occur.

## Test Cases
Unit test cases for this functionality is covered very basic file/folder operations. Run the command `pytest` to see the results. And ofcourse, there is scope for improving that. 

## Documentation

Before implementing folder-sync, some research is done and finally concluded that synchronization are generally in two forms, initial sync and delta sync (delta changes). To do this, a variable `LAST_SYNC_TIME` is used. During initial sync, all the files and folders are created in the target folder and in delta sync, only the files/folders that are changed after the last successful execution time will alone be synchronized. This will reduce the time for consecutive syncs and considered to be the most efficient and performant way of sync.

### Implementation notes

 - *No target folder in input:* the name `_replica` appending the source folder name is considered to be the target folder. eg. if source folder is `/tmp/test`, then the replica folder is at the same location `/tmp/test_replica` 
 - *Rename file/folder operations:* folder-sync does not perform rename operations the target folder if the source files/folders renamed. Rather, it deletes the target and re-creates the renamed content again. This could be improved in future.
 - *Log file:* operations are logged in the provided log file path with date, time, log level and message or exception.
 - *Metrics:* Time taken for every sync is recorded to a csv file and the results are displayed in a html file. However, more metrics like, number of files added, removed, etc could be added in future. 
 
 ## Metrics
 Folder sync metrics are capture in a csv file which is git ignored in the `meta` folder. The meta folder contains additional or metadata information about  folder-sync operations. A .html and .js file is used to represent the metrics that are captured during folder-sync operations. To verify the metrics, run the command `python metrics_manager.py`. This will create a temp.html file in meta folder and opens the folder in your default browser. Following are some of the ways the metrics are represented:
### Sync metrics table
![enter image description here](https://lh3.googleusercontent.com/Nci3CsOBJiJCcteZ14-CACzkqeGDD-MAa0LNSJ_UdrjHskFnBFlsSVcBQ3Y8SXL1JXxIN-H9aYjpXB0W3UDgQsI1s-3IjrqMZVnLxO-na7Gn0COyiAvNJfO6hvOMSQ8uhMEKyvxmbZj2Bxco8iXu5h21lfws22Z8mWvN1a4eLIRnFtBDnlpRqXNWJC_Txh4trBQUHVr4e-XQ_AsPPPGRbldrorjZrmiMDCZ6j4I0CR9_9QfQk0xwDgJM_X63UEsefa3O3yDhxC3EWuaeIvgmmGUcVijPfk0NglJgOBt4NQtWiTQ3kbPr3tX7GYyLYeP4Q5ai5axe3bndFKz97bMqD1ntgQ-evTA_ZYtBb9qCDR8X4KUxwr38K9IlsR5ixYPk2jgufiV-InLYz9sqMiAE9WktkyYq7WuEj_rsGkRXOUeMfxczWr2NJyzXpSU6Fomb7-N13BUYqSSe4ZXWY2NuOkxrnCPRA8CRUrNRTQ-Sqmaj8FFG1PNevCJnq7SD8jUcl98Ofi1_2_3TEoVOCMx-Bp-nPP5XEQ91TYVr6RIaUTvxi8RD0jQrvEJvNonY720eruL_a0SVpEJ6u9CTxCfxjsl5F9wcifNIy0KKT5ez3tRQenwcQNebPlCj8B6DNiQHR998KI_Iv_Otg3NKc0RaoTzd5XGZEYwdgayyRhz5h2WYl8tYN259lXIsT3L46QKfz3_WfPUwJI7b47Vi0J4rPLLh1XLMA5q6aFmbp3m8Z70kUEInX5d15VfmkiInhaONMYc4EK_VjyboWvPNxLATspMvWTClaDDWL1tMj-cLnI1oe8vd2w0D217WbAMogRYR7gR5K-nr5wSIV4BJuYTlF5pJ9BCddNxpO5XbV9xWZ4qxTUJ5iuKkGjtG-lK6ciQZ9P88LyBSuO-r6QVCL2Wcpb9SHc7FU6OngS84qzc=w1282-h1318-no?authuser=0)

### Sync metrics chart
![enter image description here](https://lh3.googleusercontent.com/8y3FIlJdATfuymy_je-I1N1HbeLvhU-VpmZZWM3hbuy9OFKbbClIjjVUVXfeLs1mNN2Qr_9Due-nrAaecBlDqbyFdqh8Wm7psFYOo7CJVzSM8y8rdPWOLUgbVTzfA9hQ4RHw_Z7Y_lloo5k9L2E95eJOu0F-DEFeZIwi8Zpmm6EvtFuSPvR_D8_6w9rZWE8FHmsn7YcpW2oY11PdeBXf7RomANcSCewyr8oaA_fy3YkvWTQKj1-cUC2E9W4ulyWMRIvtUxEmpXoAlZQ4krV8oqJmBFE-9AnlqVysA0eRurgkIIGysFw6Fy3moYTuDnpCHeyUjS-v_VhbNYD7jlYoZ_3541E05tBAI-KrYjy6zVqwIHI_yLnquJNbrXQWvbKd4XH8-hm2O2PYzQEQUSfyKvzV-x3kUj9RvWV0RPToAs-JgYpLofH9nD4H4NwHeqereszb6X7-LmtTqpMWN56VDtJulerlHoq1D89FCzhiNhPdy4fclLHaY-66Qj7rXdGkqLzUCrYfkifptgdQIDLGsq3kPb4FT75tnNz78z5OA_10jRhHSG3cYoik2v9MzAXMACLxkuMCygjmwt9S99ExtmLY22K4R3DezKW0E3Kq8CRiLOhvVNRB4Y-pvMOxidJF0JZxF259RvjdyIxWfkQHF7MgPYcZpXFhuS3ljOPzawa972zMB8eyEVuYmnwfqzR4gWa8QyCEvHdKzCawugprVrIT0FVZJY8isFtvg2SGAJ2iwVdTPJ-gYGi5tCgmeKlVY-i844PiN0ycwauMVeEWSBa9QANYoPyaCzneNOv-_ZxoPlSFDYZqDDmnc5BHDZcVtuUkHyh6LQxsnvxtsfA8CBl455n5c_61yuq8VotTVkM6RHOieCjnbQb1v8jswuY8IOMjWovnQL16ZuyiXwK_nXbKfbEfH8u70x27jUY=w1932-h724-no?authuser=0)

CanvasJS trail version is used for this but it is not for any official use and only for self use. As this repo belongs to me, I have chosen the trail version which is free for self use. 

More metrics like this could be added in the future. Metrics like number of files/folders affected in each and every sync, number of file deleted, created and number of folders created and deleted. Considering the time, only the time take for every sync is done. 
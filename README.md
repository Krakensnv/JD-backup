# JD-backup

## Description
JD-backup is an advanced Python script, that will extract all links from a **jDownloader 2** file list and export them to a text file.

# Thanks to:
[hherglotz](https://github.com/hherglotz/linkextractor)
for an idea and the source code, which I used as a start of my project.

## What JD-backup does
- Firstly, after executing the script, it will detect, which OS you are using for setting the **JDownloader Installation Directory PATH**.
- Secondly, the script will sort all **downloadListXXX.zip** files in the **JDownloader config** dir by date and the recent file will copy and extract to a temporary created folder **temp**.
- Next, it will extract links from all the files in **temp** and saves them to **my_jd_links.txt** file.
- Finally, the script will delete the **temp** folder.


## Prerequisites
**Default Installation PATH of JDownloader**
If you haven't installed Python on your system yet, get it directly at (https://www.python.org/).
JD-backup uses libraries `os`, `platform`, `glob`, `shutil`, `zipfile` and `json`.

## Tests:
**JD-backup** has already been tested on Windows 7, Mac OS Big Sur and Debian Buster with Python 3.8 version.
I haven't found any differencies during a backup, either JDownloader 2 was running or not.

## Installation
No special installation is needed. 

## Run the programme

Open a terminal: 
On Windows by pressing `WinKey + R` and then type `cmd` and `Enter`.
On Mac OS by pressing `Control + Backspace` then type `terminal` and press `Enter`.
On Linux by pressing `Control + Alt + T`.

Navigate to the `JD-backup-main` directory.

Then run the script by command `python3 get-jd-links.py`. 

Once it's done, you will find a new file called `my_jd_links.txt` in the `JD-backup-main` directory.

Note:
If you run the programme again, the `my_jd_links.txt` file will be overwritten.


## Recovery:
Just run jDownloader 2, open `my_jd_links.txt` file, sellect all `Control + A` then copy `Control + C` and JDownloader will import all copied links by its self.
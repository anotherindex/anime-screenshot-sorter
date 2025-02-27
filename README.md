# Index's Anime Screenshot Sorter
A simple anime screenshot sorter written in Python. Initially just a personal project but maybe someone else out there likes to take a lot of anime screenshots.    
Simply run the .py file in a folder and it will try to sort all anime screenshots into separate folders.

https://github.com/anotherindex/anime-screenshot-sorter/assets/134344244/d72808c6-dea9-4d13-803c-8fb1a3fde57d

### How-To
Download the "Index's Anime Screenshot Sorter.py" file, put it in a folder with your anime screenshots and run the file. You will need Python 3.5 or higher installed. 
Sorts .png and .jpg files.

## Possible file names and settings
### With the default settings enabled the sorter will sort any files that:
- Start with a [SubGroup] bracket.
- Have a dash, followed by an episode number, for example " - 01" somewhere in its name.

These should apply to most anime screenshots, but to broaden the accaptable file names you can change three settings:
### Screenshots must start with [SubGroup]:
The default setting is "True".    
If disabled it will also sort screenshots that do not start with a [SubGroup] bracket.    
Example: "Anime Name - 03.jpg"
### Screenshots must have an episode number:
The default setting is "True".    
If disabled it will also sort screenshots simply have a dash in its name.   
Example: "[SubGroup] Anime Title - OVA1.jpg" or "Anime Title - S01E03.jpg".   
*Be careful as disabling this can cause issues with duplicated files since Windows adds " - Copy" at the end of the filename.*
### Screenshots may have S01E01 formatting:
The default setting is "False".    
This one is a bit of an edge case. It needs "Screenshots must have an episode number" being False, but if that setting is False, it already sorts "Anime Title - S01E12.jpg".    
Enabling this however *does* allow you to sort screenshots that don't have a dash in them and are formatted as "Anime Title S01.jpg".    
Example: "Anime Title S01E104.jpg" or "[Sub Group] Anime Title S03E01.png"
### Only sort screenshots if anime folder exists:
The default setting is "False".    
If set to "True", it will only sort the screenshots into folders, if a fitting folder already exists.    
This works well if some shows from a previous season are overlapping into the new season for a couple episodes and you only want to sort those old shows for now so you can put them into a dedicated season folder.
### Overwrite Duplicates
The default setting is "False".    
If overwrite duplicates is set to "True" and the sorter tries to put a file in a folder, but a file with that exact filename is already in the folder, it will be overwritten.    
If set to "False" and a file with the exact filename is already in the target folder, both files will be stay unchanged.
### Autostart sorting when file is run:
The default setting is "False".    
If set to False you will get promptet to start the sorting with pressing Enter. If set to True it will automatically run the sorting after executing the .py file.   
## Some examples of possible screenshot names that can be sorted:
- [SubGroup] Anime Title - 03 (1080p) [1A2B3D4E].jpg
- [Sub Group] Anime Title - 03 (1080p) [1A342451] random text or.file.information.jpg
- Anime Title - 03.png
- [Sub-Group] AnimeTitle - OVA3.jpg
- [SubGroup]\_Anime\_Title\_-\_03\_(720p).png
- AnimeTitle S01E143 (1080p).jpg
## How exactly do I run this?
First you need [Python 3.5 or higher](https://www.python.org/downloads/) installed.    
Then download the screenshot sorter python file from the [releases](https://github.com/anotherindex/anime-screenshot-sorter/releases) or grab the script from the [uploaded file directly](https://raw.githubusercontent.com/anotherindex/anime-screenshot-sorter/main/Index's%20Anime%20Screenshot%20Sorter.py) and save it as a .py file.    
Put that .py file in the folder where you save your screenshots and just doubleclick it.    
If this just opens the file like a textdocument instead of executing it, you can do the following:    
Create a new textfile, write `py "name_of_the_downloaded_screenshot_sorter_file.py"` in it (with the correct filename) and save it as `screenshot_sorter.bat` and doubleclick that file.

## Misc.
- Maybe test it on a couple screenshots first or make a backup. I have not throughly tested this script on multiple machines.
- Acronym suggestions for this are not welcome.

&nbsp;

\- Index

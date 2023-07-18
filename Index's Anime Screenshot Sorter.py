import re, os, shutil

##############################################
# --- Index's Anime Screenshot Sorter v1.2 ---
# A simple Python script to sort anime screenshots into folders.
# You can change the following options by setting them to be "True" or "False".
# Make sure the first letter of "True" and "False" is capitalized.
# Github: https://github.com/anotherindex/anime-screenshot-sorter/

# The screenshot needs to have a subgroup in the beginning, like "[SubGroup] Anime Name (...)"
screenshot_must_have_subgroup = True

# The screenshot needs to have an episode number, like "Anime Name - 03"
screenshot_must_have_episode_number = True

# Allow S01E01 or S1E104 episode formatting without needing a dash in the anime title. The above setting needs to be set to False for this to work.
screenshot_can_have_season_episode_formatting = False

# Only sort screenshots if a folder for that anime already exists. (Great to sort shows that overlap into a new season and sorting new shows later.)
only_sort_screenshots_if_folder_already_exists = False

# Automatically sort when file is run without waiting for a user input
autostart = False

##############################################

# global variables
screenshot_folder = str(os.path.dirname(__file__))
file_list = os.listdir(screenshot_folder)
anime_counter = 0  # counts how many anime of the same title are currently being sorted
sort_counter = [0, 0, 0, 0]  # successfully sorted, issues with sorting, non anime, not sored due to existing folder rule
previous_anime_title = ""
sorting_prefix = "+"


def get_anime_title(full_filename):
    global previous_anime_title
    try:
        # replace all _ in the filename
        if "_" in full_filename:
            full_filename = full_filename.replace("_", " ")

        # check if the file starts with a [Sub Group]
        subgroup_regex_search = re.search("^\[[^+]*?]", full_filename)

        #determines the start of the anime title
        if bool(subgroup_regex_search):
            if full_filename[subgroup_regex_search.span(0)[1]] == " ":
                anime_title_start = subgroup_regex_search.span(0)[1] + 1
            else:
                anime_title_start = subgroup_regex_search.span(0)[1]
        elif screenshot_must_have_subgroup:
            return "doesn't meet criteria"
        else:
            anime_title_start = 0

        # check if anime has a dash followed by an episode number
        anime_title_regex_search = re.search("( - )[0-9]", full_filename)
        anime_title_season_and_episode_regex_search = re.search("\sS\d{1,3}E\d{1,3}", full_filename)
        # regex found an episode number in the format of " - 01"
        if bool(anime_title_regex_search):
            anime_title_end = anime_title_regex_search.span(0)[0]
            anime_title = full_filename[anime_title_start:anime_title_end]
        # regex found a season and episode number in the format of " S001E001", this formatting is allowed, and the screenshot must not have the classic episode number formatting
        elif screenshot_can_have_season_episode_formatting and bool(anime_title_season_and_episode_regex_search) and not screenshot_must_have_episode_number:
            # regex tries if it maybe even can find a " - S001E001" style formatting
            anime_title_regex_search = re.search("( - )S\d{1,3}E\d{1,3}", full_filename)
            if bool(anime_title_regex_search):
                anime_title_end = anime_title_regex_search.span(0)[0]
                anime_title = full_filename[anime_title_start:anime_title_end]
            else:
                anime_title_end = anime_title_season_and_episode_regex_search.span(0)[0]
                anime_title = full_filename[anime_title_start:anime_title_end]
        elif not screenshot_must_have_episode_number:
            anime_title_regex_search = re.search(".*( - )", full_filename)
            if not bool(anime_title_regex_search):
                return "doesn't meet criteria"
            anime_title_end = anime_title_regex_search.span(0)[1]
            anime_title = full_filename[anime_title_start:anime_title_end - 3]
        else:
            return "doesn't meet criteria"
        return anime_title

    except:
        print("! Issue with finding anime name")
        return "anime title issue"


def sort_file():
    global sorting_prefix, previous_anime_title, anime_counter, sort_counter

    try:
        # checks if a folder for the anime already exists, if not creates one
        if not os.path.exists(screenshot_folder + "/" + anime_title):
            if only_sort_screenshots_if_folder_already_exists:
                sorting_prefix = "-"
            else:
                os.makedirs(screenshot_folder + "/" + anime_title)
                sorting_prefix = "*"
                shutil.move(screenshot_folder + "/" + current_file, screenshot_folder + "/" + anime_title + "/" + current_file)
        elif not (sorting_prefix == "*" and previous_anime_title == anime_title):
            sorting_prefix = "+"
            shutil.move(screenshot_folder + "/" + current_file, screenshot_folder + "/" + anime_title + "/" + current_file)
        else:
            shutil.move(screenshot_folder + "/" + current_file, screenshot_folder + "/" + anime_title + "/" + current_file)

        # counting and displaying the sorting process
        if previous_anime_title == anime_title:
            anime_counter += 1
            print("\r", end="")
            print(f"{sorting_prefix} {anime_title} - x{anime_counter}", end="")
        elif previous_anime_title == "file_sorting_exception":
            print(f"\n{sorting_prefix} {anime_title}", end="")
            anime_counter = 1
        else:
            print(f"\n{sorting_prefix} {anime_title}", end="")
            anime_counter = 1
        previous_anime_title = anime_title
        if sorting_prefix == "-":
            sort_counter[3] += 1
        else:
            sort_counter[0] += 1
    except:
        # way too general except statement because I'm lazy
        if previous_anime_title == "file_sorting_exception":
            print(f"! Issue sorting {current_file}")
        else:
            print(f"\n! Could not sort: {current_file}")
            previous_anime_title = "file_sorting_exception"
        sort_counter[1] += 1


if __name__ == "__main__":
    print(f"""##### Index's Anime Screenshot Sorter v1.2 #####\n\nSettings:\nScreenshots must start with [SubGroup]:       {screenshot_must_have_subgroup}\nScreenshots must have an episode number:      {screenshot_must_have_episode_number}\nScreenshots may have S01E01 formatting:       {screenshot_can_have_season_episode_formatting}{" (Note: This setting is inactive since the above setting is set to True." if (screenshot_must_have_episode_number and screenshot_can_have_season_episode_formatting) else ""}\nOnly sort screenshots if anime folder exists: {only_sort_screenshots_if_folder_already_exists}\nAutostart sorting when file is run:           {autostart}\n(You can change these settings by opening this file in a text editor.)\n""")
    if autostart:
        print("--- Starting: ---")
    else:
        input("Press Enter to start sorting...")
        print("--- Starting: ---")
    for current_file in file_list:
        if bool(re.search(".jpg|.png", current_file)):
            anime_title = get_anime_title(current_file)
            if anime_title == "doesn't meet criteria":
                sort_counter[2] += 1
                previous_anime_title = "file_sorting_exception"
            elif anime_title == "anime title issue":
                sort_counter[1] += 1
                previous_anime_title = "file_sorting_exception"
            else:
                sort_file()
    input(f"""\n\n--- Sorting done! ---\n\nSucessfully sorted screenshots:     {sort_counter[0]}\nIssues with filename while sorting: {sort_counter[1]}\nDetected as non-anime screenshots:  {sort_counter[2]}\n{"Not sorted because of folder rule:  " if only_sort_screenshots_if_folder_already_exists else ""}{(str(sort_counter[3]))+chr(10) if only_sort_screenshots_if_folder_already_exists else ""}\n\nPress Enter to close this window...""")

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import re
import requests
import os
import itertools
import sys


class FileContent:
    
    def __init__(self, app_name, author, version, template_files, sides):

        self.name = app_name
        self.ver = version
        self.author = author
        self.file_list = template_files
        self.sides = sides

    def config_additions(self):

        for file in self.file_list:
            for line in file:
                if line.startswith("Version"):
                    i = file.index(line)
                    file.pop(i)
                    string = f"Version:{self.ver}"
                    file.insert(i, string)
                elif line.startswith("Author"):
                    i = file.index(line)
                    file.pop(i)
                    string = f"Author:{self.author}"
                    file.insert(i, string)
                elif line.startswith("Information"):
                    i = file.index(line)
                    string = file.pop(i)
                    string = string.replace("NAMEHERE", self.name)
                    file.insert(i, string)
                elif line.startswith("[NAMEHERE]"):
                    i = file.index(line)
                    string = file.pop(i)
                    string = string.replace("NAMEHERE", self.name.upper())
                    file.insert(i, string)
                elif line.startswith("ImageName"):
                    i = file.index(line)
                    string = file.pop(i)
                    string = string.replace("NAMEHERE", self.name)
                    file.insert(i, string)
                elif line.startswith("LeftMouseUpAction"):
                    i = file.index(line)
                    string = file.pop(i)
                    string = string.replace("PATHHERE", f"{self.name.upper()} PATHHERE")
                    file.insert(i, string)

    def file_creation(self):

        for side, file in itertools.product(self.sides, self.file_list):
            config = f"{self.name} {side}.ini"

            with open(config, "w") as f:
                f.writelines(file)
            

class CompleteFiles:

    def __init__(self, sides):
        self.sides = sides

    def complete_script(self):
        files = []
        for side in self.sides:
            for file in os.listdir():
                if os.path.splitext():
                    pass


class Version:
    page = requests.get("https://github.com/Ruben35/More-Icons-unFold-Rainmeter/tags").text
    page = BeautifulSoup(page, 'html.parser')
    release_number = 0

    @classmethod
    def latest(cls):

        hrefs = cls.page.findAll('a')

        for link in hrefs:
            if re.search("/releases/tag/", link['href']):
                cls.release_number = float(link.text.strip())
                break

        return cls.release_number + 1

    @classmethod
    def download_page(cls):
        
        hrefs = cls.page.findAll("a")
        link = 0

        for link in hrefs:
            if re.search("/releases/tag/", link["href"]):
                link = link["href"]
                break

        link_page = requests.get(link).text
        link_page = BeautifulSoup(link_page, "html.parser")

        hrefs = link_page.findAll('a')

        for link in hrefs:
            if re.search("/releases/download", link["href"]):
                link = link["href"]
                break

        return link


def file_read(sides):

    f_name = "Button Template.ini"
    template_files = []
    for side in sides:
        if not os.path.isfile(f"{side} Button Template.ini"):
            template_file = requests.get(f"https://raw.githubusercontent.com/feedmes1eep/small_scripts/master/"
                                         f"unFold_config_file%2Ba_bash_script/{side}%20Button%20Template.ini").content
            with open(f"{side} {f_name}", "wb") as f:
                f.write(template_file)

        with open(f"{side} {f_name}", "r") as f:
            template_files.append(f.readlines())

    return template_files


def dotenv_file(env):
    with open(".env", "a") as f:
        f.write(f"{env[0]} = {env[1]}")


def downloadSkin(page_link):

    with open("unFold.rmskin", "wb") as f:
        r = requests.get(page_link, stream=True)
        file_length = int(r.headers.get('content-length'))
        dl = 0
        left = 100 / round(file_length / 101024)
        for data in r.iter_content(chunk_size=101024):
            dl += len(data)
            print("{0:.1f} out of 100 Done".format(left), end=" ")
            left = 100 / round(file_length / len(data))
            f.write(data)
            done = int(50*dl/file_length)
            sys.stdout.write("{}{}\n".format("="*done, " "*(50-done)))
            sys.stdout.flush()


if __name__ == "__main__":

    load_dotenv()
    repo_dir = os.getenv("repo_dir")
    rain_dir = f"C:/Users/{os.getlogin()}/Documents/Rainmeter/Skins/unFold"
    if not os.path.isdir(rain_dir):
        rain_dir = None

    if not repo_dir:
        repo_dir = input("Copy the 'More-Icons-unFold-Rainmeter' directory path here: ")
        tple = ("repo_dir", repo_dir)
        dotenv_file(tple)

    if rain_dir is None and os.uname().sysname == "Linux":
        pass
    elif not os.path.isdir(rain_dir):
        print("You don't have the skin installed.")
        yn = input("I can download the file for you if you want. (Y/N): ")
        if yn == "Y" or yn == "y":
            downloadSkin(Version.download_page())
        else:
            yn = input("Proceed without skin installed? (Y/N):  ")
            if yn == "N" or yn == "n":
                print("Restart script after installing it then.")
                sys.exit(1)        

    application_name = input("Enter the Program's name: ")
    author_name = input("Author's name (GitHub name.): ")

    sides_list = ["Left", "Right"]
    t_files = file_read(sides_list)
    files = FileContent(application_name, author_name, Version.latest(), t_files, sides_list)
    files.config_additions()
    files.file_creation()

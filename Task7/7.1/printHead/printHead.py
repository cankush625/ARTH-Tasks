import pyfiglet
import os


headerTitle = pyfiglet.figlet_format("     FLEX HDFS", font="slant")
def header():
    os.system('clear')
    os.system('tput setaf 1')
    print(headerTitle)
    os.system('tput setaf 7')

from __future__ import unicode_literals
import sys, subprocess, time
try:
    import youtube_dl
except ImportError:
    importerror("youtube_dl")
# Written by manjoos
# Feel free to modify, steal, rip, and shred this code all you want..
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def main():
    ask = input(colors.HEADER+"\nWould you like download a list from a txt file? [y/n]\nEnter: "+colors.END).lower()
    if ask == "y":
        try:
            path = input(colors.HEADER+"Enter the path to the file: "+colors.END)
            file = open(path).readlines()
            for i in file:
                download(i)
        except KeyboardInterrupt:
            print(colors.WARNING+colors.BOLD+"\nCtrl + C Pressed!"+colors.END)
    elif ask == "n":
        loonk = input(colors.HEADER+"Enter the link: "+colors.END)
        download(loonk)
    else:
        print("Thats not a y or n ya dummy dum")
def download(link):
    opt = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(opt) as y:
        y.download([link])
def importerror(module):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])
if __name__ == "__main__":
    main()

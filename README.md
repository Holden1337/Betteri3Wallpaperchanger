# Betteri3Wallpaperchanger
Python script that creates a window with all of my wallpapers and allows the wallpaper to be changed in i3 without having to just open your config file in vim.
Run with 2 command line arguments. First is path to i3 config and the second one is path to wallpaper folder. This program assumes you are using feh to set your wallpaper in i3 and also that the line that sets the wallaper in i3 is the last line of the config file. I will try to change it so that you can have the feh command on any line and not that last line. Also needs tkinter, ImageTk, and Image

## Sample usage
<code>python wallchanger.py /home/username/.config/i3/config /home/username/Downloads/wallpapers </code>
  
## Sample screenshot  
![Screenshot](screenshot.png)

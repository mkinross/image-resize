# image-resize
Resize all images in a folder and save to a new sub-folder called web

This Python3 file will update all images in a folder and create and save to a new sub-folder called 'web'.

You need to edit the script by adding the path to your image folder. In Windows Explorer, browse to your image folder, and copy the path to the folder, then paste into the script. You will have change back slashes for forward slashes. And terminate the line with a forward slash.

The script will handle landscape, portrait and square images. You will need to insert the finished size in pixels for each orientation.

To use this script, you will need to install Pillow on your machine. Open your CLI (Bash, or Anaconda command propt) and type:
pip install pillow

I had to upgrade pip first. If you need to, type:
pip install --upgrade pip

If you run into 'access denied' issues, try:
pip3 install --upgrade pip --user

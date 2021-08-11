# image-resize

This Python3 script will update all images in a folder and save them to a new sub-folder called 'web'.

This works with images taken on an iPhone. I haven't tried other cameras.

Sometimes on an iPhone, landscape images are stored as portrait images. This is because smartphones don't know which way is up, and rely on accelerometer values which are stored in the images meta-data. There is a line of code in the script which attempts to access the meta-data, and correctly orientate the image. It doesn't always work!

You need to edit the script by adding the path to your image folder. In Windows Explorer, browse to your image folder, and copy the path to the folder, then paste into the script. You will have change back slashes for forward slashes. And terminate the line with a forward slash.

The script will handle landscape, portrait and square images. You will need to insert the finished size in pixels for each orientation.

To use this script, you will need to install Pillow on your machine. Open your CLI (Bash, or Anaconda command prompt) and type:
pip install pillow

I had to upgrade pip first. If you need to, type:
pip install --upgrade pip

If you run into 'access denied' issues, try:
pip3 install --upgrade pip --user

One other thing, make sure the script and all your images are running on your local computer. The script wont work if the script is running on your local computer, but all your images are in Dropbox or OneDrive, even if you specify the correct path.

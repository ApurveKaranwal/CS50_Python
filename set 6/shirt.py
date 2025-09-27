'''After finishing CS50 itself, students on campus at Harvard traditionally 
receive their very own I took CS50 t-shirt. No need to buy one online, but 
like to try one on virtually?

In a file called shirt.py, implement a program that expects exactly two
 command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as
 input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as
 output
The program should then overlay shirt.png (which has a transparent background) 
on the input after resizing and cropping the input to be the same size, saving 
the result as its output.

Open the input with Image.open, per 
pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize 
and crop the input with ImageOps.fit, 
per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
 using default values for method, bleed, and centering, overlay the shirt with 
 Image.paste, per 
 pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, 
 and save the result with Image.save, 
 per 
 pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.


The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, 
case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, 
like these demos, so that, when they’re resized and cropped, the shirt appears 
to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file
 explorer, into the same folder as shirt.py. No need to submit any photos with your code. But, if you 
 would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt
  in any of CS50’s communities!'''

  #!/usr/bin/env python3
"""
shirt.py
CS50P - P-Shirt solution

Usage:
    python shirt.py input.jpg output.jpg
    python shirt.py input.png output.png

Notes:
- input and output must both end with .jpg, .jpeg, or .png (case-insensitive)
- input and output must have the same extension
- shirt.png must be in the same directory as this script
"""

import sys
import os
from PIL import Image, ImageOps

def main():
    # 1) Check number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input.jpg output.jpg")

    infile, outfile = sys.argv[1], sys.argv[2]

    # 2) Validate extensions
    valid_exts = (".jpg", ".jpeg", ".png")
    in_ext = os.path.splitext(infile)[1].lower()
    out_ext = os.path.splitext(outfile)[1].lower()

    if in_ext not in valid_exts or out_ext not in valid_exts:
        sys.exit("Input and output must end with .jpg, .jpeg, or .png")

    # 3) Ensure input and output share the same extension
    if in_ext != out_ext:
        sys.exit("Input and output must have the same file extension")

    # 4) Ensure input file exists
    if not os.path.exists(infile):
        sys.exit("Input file does not exist")

    # 5) Locate shirt.png relative to this script (so check50 / graders can find it)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    shirt_path = os.path.join(script_dir, "shirt.png")

    if not os.path.exists(shirt_path):
        sys.exit("shirt.png not found in script directory")

    # 6) Open images and process
    try:
        shirt = Image.open(shirt_path)
    except Exception:
        sys.exit("Could not open shirt.png")

    try:
        photo = Image.open(infile)
    except Exception:
        sys.exit("Could not open input image")

    # Resize/crop the input photo to exactly the shirt size
    photo = ImageOps.fit(photo, shirt.size)

    # Paste shirt on top, using shirt's alpha channel as mask
    photo.paste(shirt, (0, 0), shirt)

    # Save the result
    try:
        photo.save(outfile)
    except Exception:
        sys.exit("Could not save output image")

if __name__ == "__main__":
    main()

# Meme Generator 

Build a meme generator that uses a list of images, and quotes, to create memes. 

## How to run

### Prerequisites 

Install the requirements:
`pip install -r requirements.txt` 

The `pdftotext` can be installed from (here)[https://www.xpdfreader.com/download.html]

## Usage 

## CLI
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR] 
Generate a meme by providing  a body (quote), author  and a path for where the image is located.

default arguments:
    - h, --help     shows this help message and exits (optional argument)
    --path PATH     the path where the image is located. 
    --body BODY     the quote to show on the image.
    --author AUTHOR the author of the quote.
   

### Web App
In the terminal run the following command from within the `src` folder:
`python3 app.py` 
This command will start the application.

In a web broser, open the following address http://127.0.0.1:5000/

## Required Modules 

### Main Modules
`main.generate_meme(path = None, body = None, author = None)`
Generate a meme given an image path, a quote and an author.

### SubModules


`generate_meme` from `meme.py`
This module creates the meme by adding a quote, and an author to an image provided by a path.

default arguments:
    --body BODY     the quote to show on the image
    --author AUTHOR the author of the quote
    --path PATH     the path where the image is located. 

`make_meme` from `MemeEngine.py` 
This module generates the actual meme image using a certain width to the images.

default arguments:
    --body BODY     the quote to show on the image
    --author AUTHOR the author of the quote
    --img_path PATH the path where the image is located. 
    --width WIDTH   the width of the image to be created

`setup` from `app.py`
This module performs the setup of the project with the quote file locations, and images path.

default arguments:
    --NONE

`meme_rand` from `app.py` 
This module generates a random meme by selecting a random quote with it's author and a random image path.

default arguments:
    --NONE

`meme_form` from `app.py`
This module allows the user to input information for a new meme: quote, author and image path from any online website. 

default arguments:
    --NONE

`meme_post` from `app.py`
This module creates the meme provided by the user  in the `meme_form` module.

default arguments:
    --NONE


# Acknowledgements
This project is part of the Udacity course Intermediate Python Nanodegree.


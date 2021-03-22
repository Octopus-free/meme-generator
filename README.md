# Meme Generator project
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.
## The application description
The application performs:

* Interacts with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
* Loads quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
* Loads, manipulate, and save images.
* Accepts dynamic user input through a command-line tool and a web service. This emulates the kind of work you’ll encounter as a full stack developer.

## Quote Engine module
This module  composed of many classes and demonstrate  understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.
The module realizes classes for parsing inputs file of several formats (txt, pdf, docx, csv).

## Meme Generator module
The module is responsible for manipulating and drawing text onto images. It demonstrates skill using a more advanced third party library for image manipulation (pillow) with the following responsibilities:

* Loading of a file from disk
* Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
* Add a caption to an image (string input) with a body and author to a random location on the image.

## Instructions for setting up and running the program
The project contains the requirements.txt file that consists of nessesary lirbraries list.
You should run:
```
pip install -r requirements.txt
```
And than run the command:
```
python app.py
```
Local html page with address `http://127.0.0.1:5000/` allows interacting with the application.
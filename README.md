# QR CODE GENERATOR

## Introduction
QR Code generator is an online software that allows users to create QR Codes by entering desired information and download them in different formats - PNG, JPG, SVG, and EPS.

## Aim
This project aims to create the best platform that allows users generate QR code for their various needs. 

## Goals
The primary goals are flexible sharing options (allow users download generated QR codes in png, jpeg, and pdf format or share the code via email / social media platforms) and promote personalised user history and archives. Secondary goals are to enhance user experience by allowing users customise generated codes to desired brand colours and good documentation comments.

## TABLE OF CONTENT

1. [SetUp](#SetUp)
2. [Walkthrough](#Walkthrough)
3. [Project Features](#ProjectFeatures)
4. [Test](#Test)

## SetUp

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/zuri-training/Project-QR-Gen-Team-52-Backend.git
$ cd "parent directory"
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/Scripts/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Walkthrough

### Authorised User Pre-authentication and Privileges 
 Upon registration 'Sign Up' a user is authorised and logged as an authenticated user with the following privileges;
 - Full access to platform
 - User is allowed to set what should happen when QR is scanned i.e
    - QR code should redirect people to a blog
    - QR code should access a document
 - Share QR code via email or social media
 - Download QR code in desired options eg Pdf, Png, Jpeg etc. 
 - Personalised Dashboard / User History.
 - Customise Qr codes to brand colours 

### Unauthorised User privileges 
An Unauthorised User are users who have not 'Signed Up' on the platform. They can do the following;
- Visit the platform to view basic information 
- View and interact with documentation 
- Register to view more details 
- They have no access to use the QR Generator until they are registered.


## Project Features

- User Registration
- Settings on QRCode enabled to be used by User
- Available options on the application:
    - Links
    - Contact Details
    - SMS
    - Videos
    - Images
    - Audio files
    - Send Email


## Test
To run the tests, `cd` into the directory that has `manage.py`, then run:
```sh
(env)$ python manage.py test app
```

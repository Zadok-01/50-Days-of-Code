# Challenge 50


from flask import Flask, render_template


app = Flask(__name__, 
            static_folder='ch50_support', 
            template_folder='ch50_support')


@app.route('/')
def home():
    return render_template('ch50_home.html')


@app.route('/about')
def about():
    return render_template('ch50_about.html')


# IMPORTANT ####
#
# Run this using < flask --app challenge_50.py run >
#
# Also required is the < ch50_support > folder containing these files:
#    ch50_home.html
#    ch50_about.html
#    style.css
#    seascape.jpg



'''
Challenge #50:

Day 50: Create a Flask App

In this challenge, you will get to create an app using Flask. Flask is a 
Python web framework. Learning to build websites with Flask is a very 
important skill to have if you want to get into web development. You will 
build an app using Python, HTML, and CSS. You are going to create an app 
with two pages, the home page and the about page. Your website will have a 
navigation bar, so you can move between the home page and the about page. 
It will have a background image.

Below is what you should make:

Flask does not come with Python so you will have to install it on your 
machine and import it into your script. If you have not made any website 
before, this challenge will require some research. I suggest using a 
virtual environment for your project. Good luck. I believe in you.
'''


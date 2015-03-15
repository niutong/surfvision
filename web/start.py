#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/about_us.html')
def about_us():
    return render_template('about_us.html')


@app.route('/values.html')
def values():
    return render_template('values.html')


@app.route('/service.html')
def service():
    return render_template('service.html')


@app.route('/advantage.html')
def advantage():
    return render_template('advantage.html')


@app.route('/guarantee.html')
def guarantee():
    return render_template('guarantee.html')


@app.route('/client_candidates.html')
def candidates():
    return render_template('candidates.html')


@app.route('/join_us.html')
def join_us():
    return render_template('join_us.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/resumes.html')
def resumes():
    return render_template('resumes.html')


@app.route('/achievements.html')
def achievement():
    return render_template('achievement.html')


if __name__ == '__main__':
    app.debug = True
    print "web start"
    app.run(host='0.0.0.0', port=80)

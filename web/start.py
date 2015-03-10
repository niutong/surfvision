#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('fuqi.html')


if __name__ == '__main__':
    app.debug = True
    print "web start"
    app.run(host='0.0.0.0', port=80)

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:18:06 2016

@author: seefood
"""
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route('/')
def index():
    
    return render_template('index.html',name='admin')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello():
    return render_template('hello-1.html', name='Xingyun', users = [{'name':"zhang"},
                                                                    {'name':"Tom"},
                                                                    {'name':"John",'hidden':True},
                                   {'name':'Lisa'},
                                  {'name':'Bob'},
                                  {'name':u"chinese中文名字"}])

@app.route('/show1/')
def show1():
    return render_template('show1.html')
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is a integer
    return 'Post %d' % post_id

@app.route('/testfilters')
def show2():
    return render_template('show2.html')

if __name__ == '__main__':
    app.run(debug=True)

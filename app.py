from flask import Flask, render_template, request, redirect, url_for
import os #importing operating system module

app = Flask(__name__)
#to stop caching static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/') #this decorator creates the home route
def home():
  techs = ['HTML', 'CSS', 'Flask', 'Python']
  name = '30 Days of Python Programming'
  return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about')
def about():
  name = '30 Days of Python Programming'
  return render_template('about.html', name=name, title='About Us')

@app.route('/post', methods= ['GET', 'POST'])
def post():
  name = 'Text Analyzer'
  if request.method == 'GET':
    return render_template('post.html', name=name, title=name)
  if request.method == 'POST':
    content = request.form['content']
    words = content.split()
    stats ={
      'characters': len(content),
      'words': len(words),
      'lines': len(content.splitlines()),
      'unique_words': len(set(w.lower().strip('.,!?;:"\'()') for w in words))
    }
    return render_template('result.html', content=content, stats=stats, title='Result')

if __name__ == '__main__':
  #for deployment we use the environ
  #to make it work for both production and development
  port = int(os.environ.get("PORT", 5000))
  app.run(debug=True, host='0.0.0.0', port=port)
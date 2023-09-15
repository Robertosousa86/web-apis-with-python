from flask import Flask, request, render_template, redirect

"""
Logic of application

1. Render the homepage with a search box and submit button
2. User submission is sent to API as a GET request
3. The API backend captures the GET request and parses the query
4. The API then redirects to Google with appropriate querystring to search for . 
"""

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/search')
def search():
    args = request.args.get('q')
    return redirect(f'https://google.com/search?q={args}')

@app.get('/search')
def get_lucky():
    args = request.args.get('s')
    return redirect(f'https://www.google.com/webhp?s={args}')

if __name__ == '__main__':
    app.run()

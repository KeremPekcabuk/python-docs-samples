# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
import cgi


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def valid_month(month):
    controlmonth = month.capitalize()
    if controlmonth in months:
        return controlmonth
    else: return None

def escape_html(s):
    return cgi.escape(s,quote=True)

# <form method="post" action="/testform">
# <input name="q" type="checkbox"></input>
form = """
<form method="post" action="testform">

<label>One
<input name="month" type="text"></input>
</label>

</br>
<input type="submit"></input>

<div style="color:red">%(error)s</div>

</form>
"""
def strchange(error):
    return (form % {"error":error})

# asdsad
# @app.route('/', methods=['GET', 'POST'])   
# def postform():    
#     """Return a friendly HTTP greeting."""
#     return strchange('')


@app.route('/', methods=['GET', 'POST'])
def hello2():
    items = request.args.getlist('food')
    return render_template('form.html',items=items)

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    # reqforkerem = request.form.get('food')
    reqforkerem = request.form.getlist('foods')
    # foods = ['a','b','c']
    return render_template('thanks.html')
    # return render_template('thanks.html',foods=reqforkerem)

        
# def postform2():    
#     if request.method == 'POST':
#         reqforkerem = request.form.get('month')
#         ret_val = valid_month(reqforkerem)
#         return ret_val


    # deneme = request
    # """Return a friendly HTTP greeting."""
    # return deneme




if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]

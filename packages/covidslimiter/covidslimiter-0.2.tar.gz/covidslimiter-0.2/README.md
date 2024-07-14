How to install: pip install covidslimiter run this command in a terminal

Usage:

from flask import Flask
from covidslimiter.decorator import rate_limited

app = Flask(name)

@app.route('/', methods=['GET', 'POST'])
@rate_limited(limit=5, period=10, max_wait_time=60)
def home():
  return "Hello World!"

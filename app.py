from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
  return "home page"
  
@app.route('/home')
def home():
  return "Home Page"
  


if __name__ == "__main__":
  app.run(debug=True ,host="0.0.0.0")

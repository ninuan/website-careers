from flask import Flask,render_template,jsonify

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 1,00,000'
  },
  {
    'id':2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id':3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  }
]

app = Flask(__name__)
@app.route("/")
def helloworld():
  return render_template("home.html", jobs = JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug = True)
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
  return "<h1>Welcome to ITIL exam</h1>"

@app.route("/modules")
def root1():
  return "<h1>COSA <br> NDC <br> PKI <br> Security Concept <br> ITIM Devops <br> Complience Audit </h1>"

@app.route("/me")
def root2():
  return "<h1>PRN: 230344223030 <br>Name: Meet Patel <br>Phone number: +91 7043198325 </h1>"
       
if __name__ == '__main__':
   app.run(port=4000,debug=True)

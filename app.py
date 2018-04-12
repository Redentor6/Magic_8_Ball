import os
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
 
app = Flask(__name__)
 
#@app.route("/")
#def index():
    #return "Flask App!"
 
#@app.route("/hello/<string:name>")
@app.route("/")
def index():
#    return name
    answers = [ "Outlook not so good",
               "It is decidedly so",
               "It is certain",
               "Signs point to yes",
               "Concentrate and ask again",
               "My sources say no",
               "Definitely need more time to think about this one",
               "As I see it, yes"  ]
    randomNumber = randint(0,len(answers)-1) 
    answer = answers[randomNumber] 
 
    return render_template(
        'test.html',**locals())
 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




#app.run(host='0.0.0.0', port=80)
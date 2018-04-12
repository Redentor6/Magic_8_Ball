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
               "As I see it, yes",
               "Don't count on it",
               "My reply is no",
               "My sources say no",
               "Very doubtful",
               "Cannot predict now",
               "Better not tell you now",
               "Ask again later",
               "Reply hazy try again",
               "Yes",
               "Outlook good",
               "Most likely",
               "You may rely on it",
               "Yes definitely",
               "Without a doubt"  ]
    randomNumber = randint(0,len(answers)-1) 
    answer = answers[randomNumber] 
 
    return render_template(
        'test.html',**locals())
 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



#top port deployment, bottom local testing
#port = int(os.environ.get('PORT', 5000))
#app.run(host='0.0.0.0', port=port)

#app.run(host='0.0.0.0', port=80)
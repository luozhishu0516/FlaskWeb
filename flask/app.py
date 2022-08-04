from flask import Flask,render_template,request
import spacy
from spacy.matcher import Matcher

def resume_cleaning(txt):
    outp=""
    outp2=""
    nlp = spacy.load("/Users/a1/PycharmProjects/pythonProject/flask/output/model-best")
    doc=nlp(txt)
    for token in doc:
        if token.ent_type_ == "Name":
            outp = outp + " " + len(token) * "*"
        else:
            outp = outp + " " + token.text
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(outp)
    for token in doc:
        if token.like_email:
            outp2 = outp2 + " " + len(token) * "*"
        elif token.ent_type_=="CARDINAL":
            outp2 = outp2 + " " + len(token) * "*"
        else:
            outp2 = outp2 + " " + token.text
    return outp2

app= Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/result",methods=["POST","GET"])
def result():
    output=  request.form.to_dict()
    name=output["name"]##Here I can take an txt file and take the txt file
    name=resume_cleaning(name)

    return render_template("index.html",name=name)

if __name__ =='__main__':
    app.run(debug=True,port=5001)
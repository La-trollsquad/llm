from flask import Flask, request, jsonify
from trollsquadAI import TrollsquadAI

app = Flask(__name__)
instance = TrollsquadAI()

@app.route("/promptToText")
def textToImage():    
    return instance.prompt_to_text("un ecureuil qui grimpe un arbre")

if __name__== "__main__":
    app.run(debug=True)
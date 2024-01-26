from flask import Flask, request, jsonify
from trollsquadAI import TrollsquadAI

app = Flask(__name__)
instance = TrollsquadAI()


@app.route("/promptToText")
def promptToText():    
    return instance.prompt_to_text(request.args.to_dict()["prompt"])

@app.route("/textToImage")
def textToImage():    
    return instance.text_to_image(request.args.to_dict())
    
@app.route("/imageToImage")
def imageToImage():    
    return instance.image_to_image(request.args.to_dict())


if __name__== "__main__":
    app.run(debug=True)
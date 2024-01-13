from flask import Flask, request, jsonify
from trollsquadAI import TrollsquadAI

app= Flask(__name__)

@app.route("/textToImage")
def home():    

    instance = TrollsquadAI()
    res = instance.text_to_image(request.args.to_dict())

    if res==True:
        return "image output.png created", 200
    else:
        return res, 500

if __name__=="__main__":
    app.run(debug=True)
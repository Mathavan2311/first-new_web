from flask import Flask , render_template, request,redirect

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        if request.form["user"]=="uno" and request.form["word"]=="ASTA":
            flag="log in"
        else:
            flag="u failed"
        return render_template("hpage.html",name=request.form["user"],status=flag)
    return render_template("hello.html")

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
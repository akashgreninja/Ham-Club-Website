from site import addpackage
from flask import Flask, render_template,request


app=Flask(__name__)

dict=[{
        
        "name":"akash",
        "description":"I am akash uday hulekal and i like to play basketball",
        "instagram":"https://www.instagram.com/ak_uh13/",
        "linkedIn":"https://www.linkedin.com/in/akash-uday-6a0b52224/",
        "facebook":"",
        "twitter":"",
        },
{
        "name":"abhishek",
        "description":"I am akashabhishek",
        "instagram":"https://www.instagram.com/abhishek",
        "linkedIn":"https://www.linkedin.com/in/abhishek",
        "facebook":"www.facebook.com",
        "twitter":"www.twitter.com",
        }
]


@app.route("/")
def home():
    return render_template("index.html")




@app.route("/board",methods=["GET","POST"])
def board():
    
        
       
    return render_template("board.html",dict=dict)
if __name__=="__main__":
    app.run(debug=True)

    
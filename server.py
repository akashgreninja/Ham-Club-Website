from site import addpackage
from flask import Flask, render_template,request
import datetime

app=Flask(__name__)

dict=[
    {
        "photo":"./static/assets/images/Bod-images/thejusvini.webp",
        "name":"Thejusvani",
        "post":"President",
        "quote":"It's all happening for a reason.",
        "instagram":"https://instagram.com/thejusvani?igshid=YmMyMTA2M2Y=",
        "linkedIn":"https://www.linkedin.com/in/t-thejusvani-1b71681b2",
        "facebook":"",
        "twitter":"https://twitter.com/thejusvani?t=wGmsuKzD1rtWUVHY1w7zJw&s=09",
    },
    {
        "photo":"./static/assets/images/Bod-images/Sampreth S.webp",
        "name":"Sampreth S",
        "post":"Vice President",
        "quote":"You must use your heart to decide the destination, but use your head to plot the journey.",
        "instagram":"https://www.instagram.com/_s.a.m.p.r.e.t.h_/",
        "linkedIn":"https://www.linkedin.com/in/sampreth-reddy/",
        "facebook":"",
        "twitter":"https://twitter.com/sampreth_reddy",
        },
    {
        "photo":"./static/assets/images/Bod-images/Velam Varsha.webp",
        "name":"V. Varsha",
        "post":"Secretary",
        "quote":"Without rain nothing grows, learn to embrace the storms of your life!",
        "instagram":"https://instagram.com/varsha___62?igshid=YmMyMTA2M2Y=",
        "linkedIn":"",
        "facebook":"",
        "twitter":"",
    },
    {
        "photo":"./static/assets/images/Bod-images/Indefinite Integral.webp",
        "name":"Supreeth",
        "post":"Joint Secretary",
        "quote":"You Smile and your surrounding smiles with you",
        "instagram":"",
        "linkedIn":"https://www.linkedin.com/in/supreeth-n-600991230/",
        "facebook":"",
        "twitter":"",
    },
    {
        "photo":"./static/assets/images/Bod-images/somya.webp",
        "name":"Soumya",
        "post":"Tresurer",
        "quote":"All you have is now.",
        "instagram":"https://www.instagram.com/_soumya.deshpande_/",
        "linkedIn":"https://www.linkedin.com/in/soumya-k-deshpande-a6b25321a",
        "facebook":"",
        "twitter":"",
        },
          {
        "photo":"./static/assets/images/Bod-images/anirudh.webp",
        "name":"Anirudh Madhav Kulkarni",
        "post":"Social Media Director",
        "quote":"You miss 100% of the shots you don’t take.",
        "instagram":"https://instagram.com/_anirudh9094_?igshid=YmMyMTA2M2Y=",
        "linkedIn":"https://www.linkedin.com/in/anirudh-madhav-9a3766191",
        "facebook":"https://www.facebook.com/anirudh.madhav.35",
        "twitter":"",
    },
        {
        "photo":"./static/assets/images/Bod-images/Mansi.webp",
        "name":"Aniketh U Achar",
        "post":"Technical Head",
        "quote":"BE REAL",
        "instagram":"https://www.instagram.com/aniketh_achar/",
        "linkedIn":"",
        "facebook":"",
        "twitter":"",
        },
            {
        "photo":"./static/assets/images/Bod-images/Swathi Mohan.webp",
        "name":"Swathi.M",
        "post":"Technical head",
        "Quote":"Never stop chasing your dreams :)",
        "instagram":"https://www.instagram.com/p/CXaVH8zFqKv7VgInQswP0sZD8OfkmJhhnhBnZE0/?igshid=YmMyMTA2M2Y=",
        "linkedIn":"",
        "facebook":"",
        "twitter":"",
    },
  
  

    {
        "photo":"./static/assets/images/Bod-images/Joshna.webp",
        "name":"Chittineni Joshna",
        "post":"Video Editor", 
        "quote":"Being happy is the greatest form of success",
        "instagram":"",
        "linkedIn":"https://www.linkedin.com/in/joshna-ch-67bb35212",
        "facebook":"",
        "twitter":"",
    },

    {
        "photo":"./static/assets/images/Bod-images/likith.webp",
        "name":"Likithraj D R",
        "post":"PR Director", 
        "quote":"ಸೋತರು ನಗುತಿರು ಸೋಲಿಸಿದವನು ಚಿಂತಿಸುವಂತೆ",
        "instagram":"https://instagram.com/likhithraj_1?igshid=YmMyMTA2M2Y=",
        "linkedIn":"",
        "facebook":"",
        "twitter":"https://twitter.com/DLikhithraj?t=OMIOGZBYRYJGNXpXzaYliw&s=09",
    },
    {
        "photo":"",
        "name":"Pranav M",
        "post":"",
        "quote":"It's time to toss the dice",
        "instagram":"https://www.instagram.com/aniketh_achar/",
        "linkedIn":"",
        "facebook":"",
        "twitter":"",
        },
    {
        "photo":"./static/assets/images/Bod-images/Prithvi Prashanth.webp",
        "name":"Prithvi",
        "post":"Event coordinator", 
        "quote":"today's actions are tomorrow's future.",
        "instagram":"https://instagram.com/prithvi._27?igshid=YmMyMTA2M2Y=",
        "linkedIn":"https://www.linkedin.com/in/prithvi-prashanth-3225b5224",
        "facebook":"",
        "twitter":"",
    },
    {
    "photo":"./static/assets/images/Bod-images/Sharath NM.webp",
    "name":"Sharath N M",
    "post":"Event coordinator",
    "quote":"Success is the best revenge. ",
    "Instagram":" https://www.instagram.com/_sharath.sharu_/",
    "linkedIn":"https://www.linkedin.com/in/sharath-nm-022939220",
    
    "facebook":"",
    "twitter":"",
       },
    {
        "photo":"./static/assets/images/Bod-images/Nishit Khamesra.webp",
        "name":"Nishit Khamesra",
        "post":"Editor", 
        "quote":"Love the life that you live,live the life that you love!",
        "instagram":"",
        "linkedIn":"https://www.linkedin.com/in/nishit-k-9aa00b128/",
        "facebook":"",
        "twitter":"",
    },
    {
        "photo":"./static/assets/images/Bod-images/aditya.webp",
        "name":"Aditya Choudhary",
        "post":"Sponsorship head",
        "quote":"The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "instagram":"https://www.instagram.com/_adi_22_/",
        "linkedIn":"https://www.linkedin.com/in/aditya-choudhary-291a67176/",
        "facebook":"https://www.facebook.com/profile.php?id=100004098726341",
        "twitter":"https://twitter.com/Aditya98359?t=t0vPYbjYp0iuWBbiuEC8Sg&s=09",
    },



    
    
    {
        "photo":"./static/assets/images/Bod-images/akash uday.webp",
        "name":"Akash Uday",
        "post":"web developer",
        "description":"I am akash uday hulekal and i like to play basketball",
        "instagram":"https://www.instagram.com/ak_uh13/",
        "linkedIn":"https://www.linkedin.com/in/akash-uday-6a0b52224/",
        "facebook":"",
        "twitter":"",
    },


]

date=datetime.datetime.now().year



@app.route("/")
def home():
    return render_template("index.html", )




@app.route("/board",methods=["GET","POST"])
def board():
    
        
       
    return render_template("board.html",dict=dict)

@app.route("/contact",methods=["GET","POST"])
def contact():
    
        
       
    return render_template("contact.html",dict=dict)

@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/login')
def login():
    return render_template('login.html')



if __name__=="__main__":
    app.run(debug=True)

    
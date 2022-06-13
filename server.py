
from cmath import e
from functools import wraps
from flask import Flask, render_template,request, url_for,flash,redirect,abort
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired
from forms import FieldForm,LoginForm,CreatePostForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_ckeditor import CKEditor
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL","sqlite:///trial-2.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] =os.environ.get("SECRET_KEY")
# "akashuday"
ckeditor = CKEditor(app)
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

db.create_all()

class Info(UserMixin,db.Model):
    __tablename__="events"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=True)
    body = db.Column(db.String(100000),nullable=True)
    

db.create_all()



def admin_only(f):
    @wraps(f)
    def decorator_func(*args,**kwargs):
        if current_user.is_anonymous or current_user.id !=1:
            return abort(403)
        return f(*args, **kwargs)    
    return decorator_func





dict_1=[
    {
        "photo":"./static/assets/images/Bod-images/principal.jpg",
        "name":"Dr.Ashwath MU",
        "post":"Principal",
        # "quote":'"It is all happening for a reason."',
        # "instagram":"https://instagram.com/thejusvani?igshid=YmMyMTA2M2Y=",
        # "linkedIn":"https://www.linkedin.com/in/t-thejusvani-1b71681b2",
        # "facebook":"",
        # "twitter":"https://twitter.com/thejusvani?t=wGmsuKzD1rtWUVHY1w7zJw&s=09",
    },
      {
        "photo":"./static/assets/images/Bod-images/teacher.webp",
        "name":"Mrs.Shilpa B",
        "post":"Faculty Co-ordinator",
        # "quote":'"It is all happening for a reason."',
        # "instagram":"https://instagram.com/thejusvani?igshid=YmMyMTA2M2Y=",
        # "linkedIn":"https://www.linkedin.com/in/t-thejusvani-1b71681b2",
        # "facebook":"",
        # "twitter":"https://twitter.com/thejusvani?t=wGmsuKzD1rtWUVHY1w7zJw&s=09",
    },
     
]

dict=[
    {
        "photo":"./static/assets/images/Bod-images/thejusvini.webp",
        "name":"Thejusvani",
        "post":"President",
        "quote":'"It is all happening for a reason."',
        "instagram":"https://instagram.com/thejusvani?igshid=YmMyMTA2M2Y=",
        "linkedIn":"https://www.linkedin.com/in/t-thejusvani-1b71681b2",
        "facebook":"",
        "twitter":"https://twitter.com/thejusvani?t=wGmsuKzD1rtWUVHY1w7zJw&s=09",
    },
    {
        "photo":"./static/assets/images/Bod-images/Sampreth S.webp",
        "name":"Sampreth S",
        "post":"Vice President",
        "quote":'"You must use your heart to decide the destination, but use your head to plot the journey."',
        "instagram":"https://www.instagram.com/_s.a.m.p.r.e.t.h_/",
        "linkedIn":"https://www.linkedin.com/in/sampreth-reddy/",
        "facebook":"",
        "twitter":"https://twitter.com/sampreth_reddy",
        },
    {
        "photo":"./static/assets/images/Bod-images/Velam Varsha.webp",
        "name":"V. Varsha",
        "post":"Secretary",
        "quote":'"Without rain nothing grows, learn to embrace the storms of your life!"',
        "instagram":"https://instagram.com/varsha___62?igshid=YmMyMTA2M2Y=",
        "linkedIn":"",
        "facebook":"",
        "twitter":"",
    },
    {
        "photo":"./static/assets/images/Bod-images/Indefinite Integral.webp",
        "name":"Supreeth",
        "post":"Joint Secretary",
        "quote":'"You Smile and your surrounding smiles with you"',
        "instagram":"",
        "linkedIn":"https://www.linkedin.com/in/supreeth-n-600991230/",
        "facebook":"",
        "twitter":"",
    },
   
    {
        
        "name":"Manish Rakshith",
        "photo":"./static/assets/images/Bod-images/Manish.jpg",
        "post":"Tresurer",
        "quote":'"IF YOU WANT TO WALK FAST, WALK ALONE. IF YOU WANT TO WALK FAR, WALK TOGETHER."',
        "instagram":"http://instagram.com/manish_rakshith?utm_source=qr",
        "linkedIn":"https://www.linkedin.com/public-profile/settings",
        "facebook":"https://www.facebook.com/Manish.Rakshith",
        "twitter":"",
        },
    {
        "photo":"./static/assets/images/Bod-images/somya.webp",
        "name":"Soumya",
        "post":"Joint Tresurer",
        "quote":'"All you have is now."',
        "instagram":"https://www.instagram.com/_soumya.deshpande_/",
        "linkedIn":"https://www.linkedin.com/in/soumya-k-deshpande-a6b25321a",
        "facebook":"",
        "twitter":"",
        },
          {
        "photo":"./static/assets/images/Bod-images/anirudh.webp",
        "name":"Anirudh Madhav Kulkarni",
        "post":"Social Media Director",
        "quote":'"You miss 100% of the shots you don’t take."',
        "instagram":"https://instagram.com/_anirudh9094_?igshid=YmMyMTA2M2Y=",
        "linkedIn":"https://www.linkedin.com/in/anirudh-madhav-9a3766191",
        "facebook":"https://www.facebook.com/anirudh.madhav.35",
        "twitter":"",
    },
    {
        "photo":"./static/assets/images/Bod-images/hemanth-2.webp",
        "name":"Hemanth BS",
        "post":"Project Head",
        "quote":"Success only comes before work...In the Dictionary.",
        "instagram":"https://www.instagram.com/_hemanth_bs_/",
        "linkedIn":"https://www.linkedin.com/in/hemanthbs",
        "facebook":"",
        "twitter":"",
        },
         { 
      "name":"Srivatsa P",
       "photo":"./static/assets/images/Bod-images/srivasta.jpeg",
      "post":"Research and Development Director",
      "quote":"Knowledge and awareness are vague, and perhaps better called illusions.",
      "instagram":"https://www.instagram.com/srivatsa_prakash/",
      "linkedin":"https://www.linkedin.com/in/srivatsa-p-47662b229/",
      "facebook":"",
      "twitter":"",
},

        {
        "photo":"./static/assets/images/Bod-images/Mansi.webp",
        "name":"Aniketh U Achar",
        "post":"Technical Head",
        "quote":'"BE REAL"',
        "instagram":"https://www.instagram.com/aniketh_achar/",
        "linkedIn":"",
        "facebook":"",
        "twitter":"",
        },
            {
        "photo":"./static/assets/images/Bod-images/Swathi Mohan.webp",
        "name":"Swathi.M",
        "post":"Technical head",
        "Quote":'"Never stop chasing your dreams :)"',
        "instagram":"https://www.instagram.com/p/CXaVH8zFqKv7VgInQswP0sZD8OfkmJhhnhBnZE0/?igshid=YmMyMTA2M2Y=",
        "linkedIn":"",
        "facebook":"",
        "twitter":"",
    },
  
  

    {
        "photo":"./static/assets/images/Bod-images/Joshna.webp",
        "name":"Chittineni Joshna",
        "post":"Video Editor", 
        "quote":'"Being happy is the greatest form of success"',
        "instagram":"",
        "linkedIn":"https://www.linkedin.com/in/joshna-ch-67bb35212",
        "facebook":"",
        "twitter":"",
    },

    {
        "photo":"./static/assets/images/Bod-images/likith.webp",
        "name":"Likithraj D R",
        "post":"PR Director", 
        "quote":'"ಸೋತರು ನಗುತಿರು ಸೋಲಿಸಿದವನು ಚಿಂತಿಸುವಂತೆ"',
        "instagram":"https://instagram.com/likhithraj_1?igshid=YmMyMTA2M2Y=",
        "linkedIn":"",
        "facebook":"",
        "twitter":"https://twitter.com/DLikhithraj?t=OMIOGZBYRYJGNXpXzaYliw&s=09",
    },
    {
        "photo":"",
        "name":"Pranav M",
        "post":"",
        "quote":'"It is time to toss the dice"',
        "instagram":"https://www.instagram.com/aniketh_achar/",
        "linkedIn":"",
        "facebook":"",
        "twitter":"",
        },
    {
        "photo":"./static/assets/images/Bod-images/Prithvi Prashanth.webp",
        "name":"Prithvi",
        "post":"Event coordinator", 
        "quote":'"today"s actions are tomorrow"s future."',
        "instagram":"https://instagram.com/prithvi._27?igshid=YmMyMTA2M2Y=",
        "linkedIn":"https://www.linkedin.com/in/prithvi-prashanth-3225b5224",
        "facebook":"",
        "twitter":"",
    },
    {
    "photo":"./static/assets/images/Bod-images/Sharath NM.webp",
    "name":"Sharath N M",
    "post":"Event coordinator",
    "quote":'"Success is the best revenge. "',
    "Instagram":" https://www.instagram.com/_sharath.sharu_/",
    "linkedIn":"https://www.linkedin.com/in/sharath-nm-022939220",
    
    "facebook":"",
    "twitter":"",
       },
    {
        "photo":"./static/assets/images/Bod-images/Nishit Khamesra.webp",
        "name":"Nishit Khamesra",
        "post":"Editor", 
        "quote":'"Love the life that you live,live the life that you love!"',
        "instagram":"",
        "linkedIn":"https://www.linkedin.com/in/nishit-k-9aa00b128/",
        "facebook":"",
        "twitter":"",
    },
    {
        "photo":"./static/assets/images/Bod-images/aditya.webp",
        "name":"Aditya Choudhary",
        "post":"Sponsorship head",
        "quote":'"The greatest glory in living lies not in never falling, but in rising every time we fall."',
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
    return render_template("index.html",is_user_in=current_user.is_authenticated )

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("index.html",is_user_in=current_user.is_authenticated )




@app.route("/board",methods=["GET","POST"])
def board():
    
        
       
    return render_template("board.html",dict=dict,dict_1=dict_1,is_user_in=current_user.is_authenticated )

@app.route("/contact",methods=["GET","POST"])
def contact():
    
        
       
    return render_template("contact.html",dict=dict)

@app.route('/events')
def events():
    all_events=Info.query.all()
    return render_template('events.html',all_events=all_events,is_user_in=current_user.is_authenticated )


@app.route('/login',methods=["POST","GET"])
def login():
    form=LoginForm()
    the_object=User.query.filter_by(email=form.email.data).first()
    if form.validate_on_submit():
        if not the_object:
            flash("please register again this email does not exist ")
            return redirect(url_for('login'))

        elif not check_password_hash(the_object.password,form.password.data):  
            flash("That password is wrong.")
            return redirect(url_for('login'))

        else:
            login_user(the_object)
            return redirect(url_for('home'))    


    return render_template('login.html',form=form,is_user_in=current_user.is_authenticated)



@app.route('/register',methods=["POST","GET"])
def register():
    form=FieldForm()
    
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("you have already registered ,Sign up")
            return redirect(url_for('login'))

        new_password=generate_password_hash(password=form.password.data, method='pbkdf2:sha256', salt_length=8)
        get_object=User(
  
        email = form.email.data,
        password = new_password,
        name = form.name.data
        )
        db.session.add(get_object)
        db.session.commit()
        login_user(get_object)

        return redirect(url_for('home'))
    return render_template('register.html',form=form,is_user_in=current_user.is_authenticated )



@app.route("/create-event",methods=["POST","GET"])
@admin_only
def add_new_post():
    form=CreatePostForm()
    if form.validate_on_submit():
        new_event=Info(
            title = form.title.data,
            body = form.body.data
        )
        try:
            db.session.add(new_event)
            db.session.commit()
        except Exception as e:
            print(e)

        return redirect(url_for('events'))

    return render_template('create_event.html',form=form,is_user_in=current_user.is_authenticated )


@app.route("/edit-post/<int:id>",methods=["POST","GET"])
@admin_only
def edit_post(id):
    the_object=Info.query.get(id)
    form=CreatePostForm(
        title = the_object.title,
        body = the_object.body
    )
    if form.validate_on_submit():
        the_object.title=form.title.data
        the_object.body=form.body.data
        db.session.commit()
        return redirect(url_for('events'))

    return render_template('create_event.html',form=form,is_user_in=current_user.is_authenticated )


@app.route("/delete/<int:id>")
@admin_only
def delete_post(id):
    the_object=Info.query.get(id)
    db.session.delete(the_object)
    db.session.commit()
    return redirect(url_for('events'))


if __name__=="__main__":
    app.run(debug=True)

    

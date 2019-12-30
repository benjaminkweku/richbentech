from flask import Flask,request,render_template,redirect,url_for
from time import sleep
import MySQLdb
conn=MySQLdb.connect(host="localhost",user="benjamin_python",password="qwekubenjamin123",db="python_test")
cur=conn.cursor()
#from flask_bootstrap import Bootstrap

#instantiating the flask app
app=Flask(__name__)
#Bootstrap(app)


#route for homepage
@app.route("/")
def index():
    return render_template("index.html")


#route for about page
@app.route("/about")
def about():
    return render_template("about.html")


#route for services page
@app.route("/services")
def services():
    return render_template("services.html")


#route for contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

#route for portfolio page
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


#route for form submit
@app.route('/send',methods=["GET","POST"])
def send():
   #flash=flash("please make sure all fields are field")
   if request.method=="POST":
        name=str(request.form['name'])
        email=str(request.form['email'])
        phone=str(request.form['phone'])
        comment=str(request.form['comment'])

        if name=="" or email=="" or phone=="" or comment=="":
            
            pass
        else:
            cur.execute('INSERT INTO richben_form(name,email,phone,comment) Values(%s,%s,%s,%s)',(name,email,phone,comment))
        #output=cur.execute('SELECT * FROM input_field')
            conn.commit()
            
            return redirect(url_for("contact"))
        


if __name__=="__main__":
    app.run(debug=True,port=5004)



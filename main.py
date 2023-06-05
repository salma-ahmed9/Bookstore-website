
from http.cookies import BaseCookie
from flask import Flask , render_template,request,redirect,url_for
app = Flask(__name__)
bookname=[]
bookprice=[]
bookcategory=[]
bookcover=[]
bookplot=[]
bookname1=[]
bookprice1=[]
bookcategory1=[]
bookcover1=[]
bookplot1=[]
bookname2=[]
bookprice2=[]
bookcategory2=[]
bookcover2=[]
count=0
@app.route('/signin')
def index():
    return render_template("signin.html")
@app.route('/home')
def index2():
    return render_template("book.html",name=bookname,price=bookprice,category=bookcategory,cover=bookcover,plot=bookplot,count=count)
@app.route('/contact')
def index3():
    return render_template("contact.html")
@app.route('/lordoftherings')
def index4():
    return render_template("lordoftherings.html",name=bookname2,price=bookprice2,category=bookcategory1,cover=bookcover2,count=count)
@app.route('/harrypotter')
def index5():
    return render_template("harrypotter.html")
@app.route('/percy')
def index6():
    return render_template("percy.html")
@app.route('/13reasons')
def index7():
    return render_template("13reasons.html")
@app.route('/hamlet')
def index8():
    return render_template("hamlet.html")   
@app.route('/oliver')
def index9():
    return render_template("oliver.html")
@app.route('/mid')
def index10():
    return render_template("mid.html")
@app.route('/government')
def index11():
    return render_template("government.html")
@app.route('/carry')
def index12():
    return render_template("carry.html")
@app.route("/Addingbooks")
def index13():
    return render_template("addbooks.html",name=bookname,price=bookprice,category=bookcategory,cover=bookcover,plot=bookplot,count=count)
@app.route("/cart.html")
def index14():
    return render_template("cart.html",name=bookname1,price=bookprice1,category=bookcategory1,cover=bookcover1,plot=bookplot1,count=count)
@app.route('/thanks',methods=["POST"])
def add1():
   return render_template("thanks.html")
@app.route('/addc',methods=["POST"])
def addc():
     new= request.form["nameofbook"]
     new1=request.form["categoryofbook"]
     new2=request.form["priceofbook"]
     new3=request.form["coverofbook"]
     global bookname1,bookplot1,bookcategory1,bookcover1,bookprice1,count
     bookname1.append(new)
     bookcategory1.append(new1)
     bookprice1.append(new2)
     bookcover1.append(new3)
     return redirect(url_for("index14"))
@app.route('/addb',methods=["POST"])
def addb():
   new= request.form["bookname"]
   new2= request.form["category"]
   new3= request.form["price"]
   new4= request.form["bookcover"]
   new5= request.form["bookplot"]
   global bookname,bookcover,bookprice,bookcategory,bookplot,count
   bookname.append(new)
   bookcategory.append(new2)
   bookcover.append(new4)
   bookprice.append(new3)
   bookplot.append(new5)
   count+=1
   return redirect(url_for('index2'))
app.run(debug=True)

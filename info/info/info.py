#!/usr/bin/env python
# coding: utf-8

# In[14]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def xyz():
    return render_template("saif.html")
@app.route("/detail",methods=['GET','POST'])
def abc():
    if(request.method=='POST'):
        a=int(request.form['num1'])
        b=int(request.form['num2'])
        total=a+b
        return render_template("saif.html",result=total)
if __name__=="__main__":
    app.run()

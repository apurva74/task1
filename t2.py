from flask import Flask,request, render_template
import pyshorteners
app=Flask(__name__)

@app.route('/')  #app routing
#used to map the specific URL with the associated function that is intended to perform some task. 
def home():# in this you need to render the template called the home.html
    if request.method=='GET':
        url=request.args['name']
        s=pyshorteners.Shortener()
        shorter=s.tinyurl.short(url)
        return shorter
    
    
    return render_template('home.html')
if __name__=='__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

#instantiating an object to run my flask module
app=Flask(__name__, template_folder ='templates', static_url_path="")

@app.route('/')

def home():
    return render_template("home.html")

@app.route('/')

def root():
    return app.send_static_file('home.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload=True
    app.config['TEMPLATE_AUTO_RELOAD']=True
    app.run(debug=True)
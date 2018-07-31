from flask import Flask, render_template

# create flask app
app = Flask(__name__)

# return rendered template
@app.route("/")
def main():
    return render_template('homepage.htm')

# check if the executed file is the main program and run the app
if __name__ == "__main__":
    app.debug = True
    app.run()
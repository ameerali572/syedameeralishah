from flask import Flask, render_template

# Create a Flask web application
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello():
    return render_template('index.html')

# Run the application if this file is the main program
if __name__ == '__main__':
    app.run(debug=True)


print("done")





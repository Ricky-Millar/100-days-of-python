from flask import Flask

app = Flask(__name__)



def make_bold(input):
    def make_bold_wrapper():
        message = "<b>"
        message += input()
        message += "</b>"
        return message
    return make_bold_wrapper
def make_emf(input):
    def make_bold_wrapper():
        message = "<em>"
        message += input()
        message += "</em>"
        return message
    return make_bold_wrapper



@app.route('/')
@make_bold
@make_emf
def hello_world():
    return 'Hello World banana!'

@app.route('/banana/<entry>')
def FourOFour(entry):
    return f'{entry} is not a real page, 404'

if __name__ == '__main__':
    #this restarts the server when new code is saved and also opens up other debug tools
    app.run(debug=True)
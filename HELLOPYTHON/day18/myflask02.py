from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def home():
    
    dan = request.args.get("dan")
    
    result = "";
    
    for i in range(1,10):
        
        result += str(int(dan)) + " * " + str(int(i)) + " = " + str(int(dan) * i)+'<br>'
         
    return result

if __name__ == '__main__':
    app.run(debug=True)
    
    
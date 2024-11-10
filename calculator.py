from flask import Flask, request,jsonify
app = Flask(__name__)
def calculator(operation,num1,num2):
    if operation =="Add":
        return num1+num2

    elif operation =="subtract":
        return num1-num2
    
    elif operation =="multiply":
        return num1-num2
    
    elif operation =="divide":
        return num1-num2
   
@app.route('/calculate', methods=['GET'])   
    
def calculate(): 
    operation = request.args.get('operation')
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
        
        
if operation is None or num1 is None or num2 is None:
     return jsonify({'error': 'Missing data'})
 


result = calculator(operation, float(num1), float(num2))

return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)





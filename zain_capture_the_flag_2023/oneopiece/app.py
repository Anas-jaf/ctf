from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

files = {
    'secret_file' : "flag_redacted.txt",
    'app_file': 'app.py'
}

@app.route('/execute', methods=['POST'])
def execute():
    opcodes = request.form['opcodes'].split(',')
    func = Utils(files['secret_file'],files['app_file'])
    memory = {}
    pointer = 0
    output = ""
    while pointer < len(opcodes):
        opcode = opcodes[pointer]
        if opcode == "1": 
            pointer += 1
            address = int(opcodes[pointer])
            pointer += 1
            value = opcodes[pointer]
            memory[address] = value
        elif opcode == "2":  
            pointer += 1
            address = int(opcodes[pointer])
            output += str(memory[address]) + "\n"
        elif opcode == "3":  
            pointer += 1
            filename = opcodes[pointer]
            pointer += 1
            address = int(opcodes[pointer])
            with open(re.sub(r"(?i)app\.py", "", filename), 'r') as file:
                content = file.read()
                memory[address] = content
        elif opcode == "8": 
            template_address = int(opcodes[pointer])
            pointer += 1
            title_address = int(opcodes[pointer])
            pointer += 1
            text_address = int(opcodes[pointer])
            temp = memory[title_address]
            text = memory[text_address]
            result = func.renderSTR( temp, text)
            output_address = int(opcodes[pointer])+1
                      
            memory[output_address] = result
        elif opcode == "0":  
            break

        pointer += 1
    print(memory)
    return output


class Utils(object):
    def __init__(self,secret,app):
        self.secret_file = secret
        self.restricted = app


    def renderSTR(self, temp, text):
        return temp.format(self=self,text=text)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
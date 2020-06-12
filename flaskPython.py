#from flask import Flask, jsonify, request

#app = Flask(__name__)

#userAccounts = [{"Name": 'Matthew'}, {"Name": 'Matthew'}, {"Name": 'Team13'}]

# YT Video:

'''
@app.route('/')
def index():
    return '<h4> Welcome to Account Registration</4>'

'''


#@app.route('/', methods=['GET'])
#def test():
    #return jsonify({'Message': 'It Works!!!'})


'''
#Working Get Request:
@app.route('/accountManagement1', methods=['GET'])
def returnOneVar():
    if request.method == 'GET':
    #accts = [userAccount for userAccount in userAccounts if userAccount['Name'] == Name]
        return jsonify(Name = 'Matthew')
@app.route('/accountManagement1/<string:NameOrEmail>', methods=['GET'])
def returnOneVar(NameOrEmail):
    if request.method == 'GET':

        for userAccount in userAccounts:
            if (userAccount['NameOrEmail'] == Name):
            # accts = [userAccount for userAccount in userAccounts if userAccount['Name'] == Name]
                return jsonify(Name=Name)


            if (userAccount['NameOrEmail'] == Name):
        #accts = [userAccount for userAccount in userAccounts if userAccount['Name'] == Name]
                return jsonify(Name = Name)
'''


# Working Get Request Using Data Entry in the url and a loop to parse the data
#@app.route('/accountManagement1/<string:Name>', methods=['GET'])
'''def returnOneVar(Name):
    if request.method == 'GET':

        for userAccount in userAccounts:
            if (userAccount['Name'] == Name):
                # accts = [userAccount for userAccount in userAccounts if userAccount['Name'] == Name]
                return jsonify(Name=Name)


@app.route('/accountManagement1', methods=['POST'])
def addOne():
    if request.method == 'POST':
        # useraccount = {"Name": request.get_json['Name']}
        useraccount = request.get_json['Name']
        userAccounts.append(useraccount)

        # return jsonify({'userAccounts' : })
        return jsonify({'userAccounts'})


'''
'''@app.route('/accountManagement', methods=['POST'])
def addOne():
    userAccount = {'Name' : request.json['Name']}
    userAccounts.append(userAccount)
    return jsonify('userAccounts', userAccounts)


#Flask API:

@app.route("/", methods=['GET', 'POST'])
def accountcreation():
    if request.method == 'POST':
        return jsonify({'Your': 'Account Was Created'})


@app.route("/", methods=['GET', 'POST'])
def accountcreation():
    if request.method == 'POST':
        return jsonify({'Your': 'Account Was Created'})
'''
'''if __name__ == "__main__":
    app.run(debug=True, port=5050)



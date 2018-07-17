import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response

#Flask app should start in global layout
app = Flask(_name_)

@app.route('/webhook',methods=['POST'])
def webhook():
  req = request.get_json(silent=True, force=True)
  print('Request:')
  print(json.dumps(req, indent=4))
  res = makeWebhookResult(req)
  res = json.dumps(res, indent = 4)
  print(res)
  r = make_response(res)
  r.headers['Content-Type'] = 'application/json'
  return r 

  def makeWebhookResult(req):
    if req.get('result').get('action') != 'account.balance.check':
      return {}
    result = req.get('result')
    parameters = result.get('parameters')
    name = parameters.get('name')
    cost = {'John': '$5,425','Mary': '$6,425','Susan': '$7,425','Josh': '$8,425','Michael': '$9,425'}
    speech = 'The balance of' + name + ' is ' + str(bank[name])
    print('Response:')
    print(speech)
    return{
      'speech': speech,
      'displayText': speech,
      'source': 'account.balance.check'

    }
  
if  _name_ == '__main__':
    port = int(os.getenv('PORT', 80))
    print('Starting app on port %d' %(port))
    app.run(debug=True, port=port, host='0.0.0.0')


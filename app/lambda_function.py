import json
import urllib3
import database

db_provider = database.DBProvider('tlgmUsers', 'tlgmSettings')

def send_message(text, chat_id):
    http = urllib3.PoolManager()
    token = db_provider.get_token(1)
    if token != '':
        url = "https://api.telegram.org/bot{}/sendMessage?text={}&chat_id={}".format(token, text, chat_id)
        res = http.request('GET', url)
        return res.status

def lambda_handler(event, context):
    response = ''
    status = 200
    
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    command = message['message']['text']
    
    if command.split()[0] == '/login':
        if db_provider.check_user(command.split()[1], command.split()[2]):
            db_provider.update_chatid(command.split()[1], chat_id)
            response = 'I am listening, my friend'
        else:
            response = 'User or password is incorrect'

    if command.split()[0] == '/create':
        db_provider.create_user(command.split()[1], command.split()[2])
        response = 'User {} has been created'.format(command.split()[1])

    if command.split()[0] == '/chatid':
        response = chat_id
    
    if command.split()[0] == '/do':
        if db_provider.check_chatid(chat_id):
            response = 'Some usefull action has been done'
        else:
            response = 'I do not know who you are! Please, log in!'
    
    if response != '':
        status = send_message(response, chat_id)
        
    return {
        'statusCode': status
    }
import boto3
from boto3.dynamodb.conditions import Attr


class DBProvider():
    
    def __init__(self, user_table, settings_table):
        # Get the service resource.
        dynamodb = boto3.resource('dynamodb')
        # Open the table
        self.user_table = dynamodb.Table(user_table)
        self.settings_table = dynamodb.Table(settings_table)
    
    def check_user(self, name, passwd):
        status = False

        if name and passwd:
            response = self.user_table.get_item(
                Key={
                    'user_id': name
                })
            if 'Item' in response:
                item = response['Item']
                if 'password' in item and item['password'] == passwd:
                    status = True

        return status

    def update_chatid(self, name, chat_id):
        status = False

        self.user_table.update_item(
            Key={
                'user_id': name
            },
            UpdateExpression='SET chat_id = :val1',
            ExpressionAttributeValues={
                ':val1': chat_id
            })

    def check_chatid(self, chat_id):
        status = False
        response = self.user_table.scan(
            FilterExpression=Attr('chat_id').eq(chat_id)
        )
        items = response['Items']
        if len(items) != 0:
            status = True
    
        return status
    
    def create_user(self, name, passwd):
        
        res = self.user_table.put_item(
            Item={
                'user_id': name,
                'password': passwd,
            })  

    def get_token(self, bot_id):
        token = ''
        response = self.settings_table.get_item(
            Key={
                'bot_id': bot_id
            })

        if 'Item' in response and 'token' in response['Item']:
            token = response['Item']['token']

        return token

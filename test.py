import unittest
from unittest.mock import patch, Mock
from app.database import DBProvider

class DBProviderTest(unittest.TestCase):
    @patch('app.database.boto3.resource')
    def test_check_user_correct_pswd(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'chat_id': 1044617899, 'password': 'test123', 'user_id': 'dima'},
                                            'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')    
        self.assertTrue(db_provider.check_user("dima", "test123"))

    @patch('app.database.boto3.resource')
    def test_check_user_no_user(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')    
        self.assertFalse(db_provider.check_user("dima", "test123"))

    @patch('app.database.boto3.resource')
    def test_check_user_wrong_pswd(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'chat_id': 1044617900, 'password': 'hc1234', 'user_id': 'dima'},
                                            'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')    
        self.assertFalse(db_provider.check_user("dima", "test123"))

    @patch('app.database.boto3.resource')
    def test_check_user_no_pswd(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'chat_id': 1044617900, 'user_id': 'dima'},
                                            'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')    
        self.assertFalse(db_provider.check_user("dima", "test123"))

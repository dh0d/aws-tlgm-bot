import unittest
from unittest.mock import patch, Mock
from app.database import DBProvider

class DBProviderTest(unittest.TestCase):
    @patch('app.database.boto3.resource')
    def test_check_user_correct_pswd(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'chat_id': 1044617899, 'password': 'pwd', 'user_id': 'user_1'},
                                            'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')
        self.assertTrue(db_provider.check_user("user_1", "pwd"))

    @patch('app.database.boto3.resource')
    def test_check_user_no_user(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')
        self.assertFalse(db_provider.check_user("user_1", "pwd"))

    @patch('app.database.boto3.resource')
    def test_check_user_wrong_pswd(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'chat_id': 1044617900, 'password': 'pwd', 'user_id': 'user_1'},
                                            'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')
        self.assertFalse(db_provider.check_user("user_1", "wrong_pwd"))

    @patch('app.database.boto3.resource')
    def test_check_user_no_pswd(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'chat_id': 1044617900, 'user_id': 'user_1'},
                                            'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')
        self.assertFalse(db_provider.check_user("user_1", "pwd"))

    @patch('app.database.boto3.resource')
    def test_check_user_without_pswd(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'chat_id': 1044617900, 'user_id': 'user_1'},
                                            'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')
        self.assertFalse(db_provider.check_user("user_1", ""))

    @patch('app.database.boto3.resource')
    def test_check_user_empty_pswd(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'chat_id': 1044617900, 'password': 'pwd', 'user_id': 'user_1'},
                                            'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')
        self.assertFalse(db_provider.check_user("user_1", ""))

    @patch('app.database.boto3.resource')
    def test_check_user_empty_user(self, mock_dynamodb):
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'chat_id': 1044617900, 'password': 'pwd', 'user_id': 'user_1'},
                                            'ResponseMetadata': {}}
        mock_dynamodb.return_value.Table.return_value = mock_table

        db_provider = DBProvider('tlgmUsers', 'tlgmSettings')
        self.assertFalse(db_provider.check_user("", ""))

if __name__ == '__main__':
    unittest.main()

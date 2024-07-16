import unittest
import json
from docusearch.app import process_query

class DocusearchTestCase(unittest.TestCase):
    def test_query_success(self):
        payload = {
            "query": "What was Travis Kalanick's greatest strength",
            "api_key": "sk-proj-F1DA420MC1ViQbJ6YcEPT3BlbkFJsmmzSlg0Hj4OHJynwV6V",
            "folder_path": "C:/Users/asay/OneDrive - Genmab/Desktop/Upload_Documents"
        }
        result = process_query(payload['query'], payload['api_key'], payload['folder_path'])
        self.assertIn("document_source", result)
        self.assertIn("answer", result)

    def test_missing_query(self):
        payload = {
            "api_key": "sk-proj-F1DA420MC1ViQbJ6YcEPT3BlbkFJsmmzSlg0Hj4OHJynwV6V",
            "folder_path": "C:/Users/asay/OneDrive - Genmab/Desktop/Upload_Documents"
        }
        with self.assertRaises(ValueError):
            process_query("", payload['api_key'], payload['folder_path'])

    def test_invalid_folder_path(self):
        payload = {
            "query": "Who is Travis Kalanick",
            "api_key": "sk-proj-F1DA420MC1ViQbJ6YcEPT3BlbkFJsmmzSlg0Hj4OHJynwV6V",
            "folder_path": "/invalid/path"
        }
        with self.assertRaises(FileNotFoundError):
            process_query(payload['query'], payload['api_key'], payload['folder_path'])

if __name__ == '__main__':
    unittest.main()

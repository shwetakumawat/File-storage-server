#TEST CODE TO ILLUSTRATE ITS ROBUSTNESS

import os
import unittest
import tempfile
import json
from fsstore1 import application


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, application.config['DATABASE'] = tempfile.mkstemp()
        application.config['TESTING'] = True
        self.app = application.test_client()
        with application.app_context():
            pass

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(application.config['DATABASE'])

    def test_upload_file(self):
        
        with tempfile.NamedTemporaryFile(suffix='.txt') as fp:
            fp.write(b'Test file contents')
            fp.seek(0)

            
            data = {
                'file': (fp, 'test.txt')
            }
            response = self.app.post('/files', data=data, content_type='multipart/form-data')

            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All good', response.data)

    def test_delete_file(self):
        
        with tempfile.NamedTemporaryFile(suffix='.txt') as fp:
            fp.write(b'Test file contents')
            fp.seek(0)
            filename = os.path.basename(fp.name)

            
            data = {
                'file': (fp, filename)
            }
            self.app.post('/files', data=data, content_type='multipart/form-data')

            
            response = self.app.delete(f'/files/{filename}')

            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All good', response.data)

    def test_list_files(self):
    
        response = self.app.get('/files')

        
        self.assertEqual(response.status_code, 200)
        files = json.loads(response.data.decode('utf-8'))
        self.assertIsInstance(files, list)


if __name__ == '__main__':
    unittest.main()

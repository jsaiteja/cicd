from ..flask_api.app import flask_jenkins_app
import unittest
from werkzeug.test import create_environ, run_wsgi_app
class TestCompInitTimePeriods(unittest.TestCase):
    def test_A_health_check(self):
        environ_1 = create_environ('/health-check')
        result = run_wsgi_app(flask_jenkins_app, environ_1, True)
        self.assertEqual(result[0], [b'{"Message":"Server is alive"}\n'])

    def test_B_get(self):
        environ_2 = create_environ("/lang")
        result = run_wsgi_app(flask_jenkins_app, environ_2, True)
        self.assertEqual(result[0], [b'{"languages":[{"name":"python"},{"name":"java"},{"name":"javascript"}]}\n'])

    def test_C_post(self):
        data = {"method": "POST", "json": {"name": "c"}}
        environ = create_environ("/lang", **data)
        result = run_wsgi_app(flask_jenkins_app, environ, True)
        self.assertEqual(result[0],
                     [b'{"languages":[{"name":"python"},{"name":"java"},{"name":"javascript"},{"name":"c"}]}\n'])
    def test_E_put(self):
        data = {"method": "PUT", "json": {"name": "Go"}}
        environ_4 = create_environ("/lang/python", **data)
        result = run_wsgi_app(flask_jenkins_app, environ_4, True)
        self.assertEqual(result[0], [b'{"languages":[{"name":"Go"},{"name":"java"},{"name":"javascript"}]}\n'])
    def test_F_delete(self):
        data = {"method": "DELETE"}
        environ_5 = create_environ("/lang/java", **data)
        result = run_wsgi_app(flask_jenkins_app, environ_5, True)
        self.assertEqual(result[0], [b'{"languages":[{"name":"python"},{"name":"javascript"}]}\n'])

if __name__ == '__main__':
    unittest.main()

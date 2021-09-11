from engine.tests import *


class UserResourceTest(ProjectTest):
    def setUp(self):
        super().setUp()

    def test_get_all(self):
        users = create_user()
        with Client() as client:
            response = client.get('/views', format="json")
            self.assertEqual(response.status_code, 200)
            user = User.objects.get(id=users)
            expected = {"users": [user.serialized]}
            self.assertEqual(response.json, expected)

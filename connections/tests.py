from django.test import TestCase, Client


class ConnectedDevsTestCase(TestCase):
    def setUp(self):
        # Here should be a set-up of the testing data but Twitter didn't provide
        # the permission to use their API, so I can't populate the db.
        self.dev_1_id = None
        self.dev_2_id = None
        self.client = Client()

    def test_realtime(self):
        response = self.client.get("/connected/realtime/{}/{}".format(self.dev_1_id, self.dev_2_id))
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get("/connected/register/{}/{}".format(self.dev_1_id, self.dev_2_id))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        # No set-up => no tear-down
        pass

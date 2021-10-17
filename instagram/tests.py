from django.test import TestCase
from .models import Profile,Image

# Create your tests here.
class ProfileTestCase(TestCase):

    # Set up method
    def setUp(self):
        self.duke= Profile(name='Heisting')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.duke,Profile))
        
    # Testing save method
    def test_save_method(self):
        self.duke.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    # Test delete method
    def test_delete_method(self,id):
        self.duke.delete_profile(id='')
        profile = Profile.objects.all(id)
        self.assertTrue(len(profile) == 0)
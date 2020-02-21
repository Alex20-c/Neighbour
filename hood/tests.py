from django.test import TestCase
from .models import Neighbourhood,Business,Profile

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(neighbourhood = 'Roasters')

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save(self):
        self.neighbourhood.save_neighbourhood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood)>0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(neighbourhood = 'Roasters')
        self.neighbourhood.save_neighbourhood()

        self.john = Profile(avatar = '/avatar/default.png',description = 'happy neighbour',neighbourhood = 'roasters',username = 'Ciku',name='Wanjiku',email='ciku@user.com')

    def test_save(self):
        self.john.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        


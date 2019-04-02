# -*- coding: utf-8 -*-

from django.test import TestCase
from skeleton.models import *
from django.core.management import call_command
import os


class BirdTest(TestCase):
    @classmethod
    def setUpClass(cls):
        call_command('loaddata', os.path.join('data', 'birds.json'))
        cls.bird_count = Bird.objects.count()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_at_least_one_bird(self):
        print(f'The database has {self.bird_count} bird{{}}.'.format('' if self.bird_count == 1 else 's'))
        self.assertTrue(self.bird_count > 0, 'Not enough birds; at least one bird is expected.')

    def test_bird_airspeed(self):
        self.bird = Bird.objects.sample()[0]
        airspeed = self.bird.airspeed()

        print(f'The airspeed velocity of an unladen {self.bird.common_name.title()} ({self.bird.scientific_name.title()}) is {airspeed} m/s.')
        self.assertIsInstance(airspeed, float)
        self.assertTrue(airspeed > 0, 'Birds must have an airspeed greater than 0 m/s to stay in the air.')

from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'testuser', 'email': 'test@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class TeamTests(APITestCase):
    def test_create_team(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        url = reverse('team-list')
        data = {'name': 'Test Team', 'members': [user.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        url = reverse('activity-list')
        data = {'user': user.id, 'activity_type': 'run', 'duration': 30, 'calories_burned': 200, 'date': '2024-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        url = reverse('workout-list')
        data = {'user': user.id, 'name': 'Pushups', 'description': 'Do 20 pushups'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        url = reverse('leaderboard-list')
        data = {'team': team.id, 'score': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

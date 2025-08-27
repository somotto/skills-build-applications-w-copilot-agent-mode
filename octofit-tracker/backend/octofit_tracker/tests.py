from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', activity_type='Run', duration=30, team='Test Team')
        self.assertEqual(activity.activity_type, 'Run')

    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Yoga', difficulty='Easy')
        self.assertEqual(workout.name, 'Yoga')

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

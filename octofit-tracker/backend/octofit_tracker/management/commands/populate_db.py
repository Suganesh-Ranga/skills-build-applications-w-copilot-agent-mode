from django.core.management.base import BaseCommand
from octofit_tracker.mongo import get_mongo_db

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = get_mongo_db()
        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Teams
        marvel = {'name': 'Team Marvel'}
        dc = {'name': 'Team DC'}
        marvel_id = db.teams.insert_one(marvel).inserted_id
        dc_id = db.teams.insert_one(dc).inserted_id

        # Users (superheroes)
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_id},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team_id': marvel_id},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': marvel_id},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_id},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team_id': dc_id},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_id},
        ]
        db.users.insert_many(users)
        db.users.create_index('email', unique=True)

        # Activities
        activities = [
            {'user': 'Iron Man', 'activity': 'Running', 'duration': 30},
            {'user': 'Batman', 'activity': 'Cycling', 'duration': 45},
            {'user': 'Superman', 'activity': 'Swimming', 'duration': 60},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'team': 'Team Marvel', 'points': 150},
            {'team': 'Team DC', 'points': 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user': 'Iron Man', 'workout': 'Pushups', 'reps': 50},
            {'user': 'Wonder Woman', 'workout': 'Squats', 'reps': 100},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))

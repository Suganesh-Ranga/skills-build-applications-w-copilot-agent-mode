from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mongo import get_mongo_db
from bson import ObjectId

# Helper to convert ObjectId to string
def fix_id(doc):
    if doc and '_id' in doc:
        doc['_id'] = str(doc['_id'])
    return doc

class UsersList(APIView):
    def get(self, request):
        db = get_mongo_db()
        users = list(db.users.find())
        for u in users:
            fix_id(u)
            if 'team_id' in u:
                u['team_id'] = str(u['team_id'])
        return Response(users)

class TeamsList(APIView):
    def get(self, request):
        db = get_mongo_db()
        teams = list(db.teams.find())
        for t in teams:
            fix_id(t)
        return Response(teams)

class ActivitiesList(APIView):
    def get(self, request):
        db = get_mongo_db()
        activities = list(db.activities.find())
        for a in activities:
            fix_id(a)
        return Response(activities)

class LeaderboardList(APIView):
    def get(self, request):
        db = get_mongo_db()
        leaderboard = list(db.leaderboard.find())
        for l in leaderboard:
            fix_id(l)
        return Response(leaderboard)

class WorkoutsList(APIView):
    def get(self, request):
        db = get_mongo_db()
        workouts = list(db.workouts.find())
        for w in workouts:
            fix_id(w)
        return Response(workouts)

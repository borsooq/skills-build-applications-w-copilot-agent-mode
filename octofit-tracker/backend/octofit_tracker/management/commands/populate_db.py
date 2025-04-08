from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
import logging

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)

        try:
            # Clear existing data
            logger.debug("Clearing existing data...")
            User.objects.all().delete()
            Team.objects.all().delete()
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()

            # Create users
            logger.debug("Creating users...")
            users = [
                User(username='john_doe', email='john@example.com', password='password123'),
                User(username='jane_doe', email='jane@example.com', password='password123'),
            ]
            User.objects.bulk_create(users)

            # Create teams
            logger.debug("Creating teams...")
            team = Team(name='Team Alpha')
            team.save()
            team.members.add(*users)

            # Create activities
            logger.debug("Creating activities...")
            activities = [
                Activity(user=users[0], activity_type='Running', duration=timedelta(minutes=30)),
                Activity(user=users[1], activity_type='Cycling', duration=timedelta(minutes=45)),
            ]
            Activity.objects.bulk_create(activities)

            # Create leaderboard entries
            logger.debug("Creating leaderboard entries...")
            leaderboard_entries = [
                Leaderboard(user=users[0], score=100),
                Leaderboard(user=users[1], score=90),
            ]
            Leaderboard.objects.bulk_create(leaderboard_entries)

            # Create workouts
            logger.debug("Creating workouts...")
            workouts = [
                Workout(name='Morning Run', description='A quick morning run to start the day'),
                Workout(name='Evening Cycle', description='Cycling in the evening to relax'),
            ]
            Workout.objects.bulk_create(workouts)

            logger.info("Successfully populated the database with test data.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise
# portfolio/migrations/0002_seed_profile_data.py
from django.db import migrations
from datetime import date

def create_initial_profile(apps, schema_editor):
    # Get models from the historical app registry
    Profile = apps.get_model('portfolio', 'Profile')
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')
    Experience = apps.get_model('portfolio', 'Experience')
    Education = apps.get_model('portfolio', 'Education')

    # --- Create the main Profile ---
    my_profile = Profile.objects.create(
        name="Aryan Suthar",
        email="aryansuthar71@gmail.com",
        bio="A passionate developer building cool things and a Competitive Programming enthusiast.",
        github_url="https://github.com/Ary778",
        linkedin_url="https://linkedin.com/in/aryansuthar/",
        portfolio_url="https://aryansuthar.com"
    )

    # --- Create Skills ---
    skills_to_add = ['Python', 'Django', 'JavaScript', 'React', 'PostgreSQL', 'Docker', 'Competitive Programming', 'Data Structures and Algorithms']
    for skill_name in skills_to_add:
        Skill.objects.create(profile=my_profile, name=skill_name, level="Advanced")

    # --- Create Projects ---
    Project.objects.create(
        profile=my_profile,
        title="Me-API Playground",
        description="A personal API project for a technical assessment built with Django and DRF.",
        github_link="https://github.com/Ary778/me-api-playground",
        live_url="https://your-live-project-url.com"
    )

    # --- Create Work Experience ---
    Experience.objects.create(
        profile=my_profile,
        company="Jabsz Studios",
        position="Web Development Intern",
        start_date=date(2025, 8, 1),
        end_date=None
    )

    # --- Create Education ---
    Education.objects.create(
        profile=my_profile,
        school="Pandit Deendayal Energy University",
        degree="Bachelor of Technology in Information and Communication Technology",
        start_date=date(2023, 8, 1),
        end_date=date(2027, 7, 1)
    )

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_profile),
    ]
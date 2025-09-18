# portfolio/serializers.py
from rest_framework import serializers
from .models import (
    Profile, Skill, Project, Experience, Education, Certification, Award
)

# --- Child Serializers ---
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ['profile']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['profile']

# Completed child serializers
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        exclude = ['profile']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ['profile']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        exclude = ['profile']

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        exclude = ['profile']


# --- Main Profile Serializer ---
class ProfileSerializer(serializers.ModelSerializer):
    # This part is for READING data (GET requests)
    skills = SkillSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    certifications = CertificationSerializer(many=True, read_only=True)
    awards = AwardSerializer(many=True, read_only=True)

    # This part is for WRITING data (PUT/POST requests)
    skills_data = SkillSerializer(many=True, write_only=True, required=False)
    projects_data = ProjectSerializer(many=True, write_only=True, required=False)
    experiences_data = ExperienceSerializer(many=True, write_only=True, required=False)
    educations_data = EducationSerializer(many=True, write_only=True, required=False)
    certifications_data = CertificationSerializer(many=True, write_only=True, required=False)
    awards_data = AwardSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Profile
        fields = [
            'id', 'name', 'email', 'bio', 'github_url', 'linkedin_url',
            'portfolio_url', 'skills', 'projects', 'experiences', 'educations',
            'certifications', 'awards', 'skills_data', 'projects_data',
            'experiences_data', 'educations_data', 'certifications_data', 'awards_data'
        ]

    def update(self, instance, validated_data):
        # Update simple fields on the Profile model
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.github_url = validated_data.get('github_url', instance.github_url)
        instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)
        instance.portfolio_url = validated_data.get('portfolio_url', instance.portfolio_url)
        instance.save()

        # Helper function to update one-to-many relationships
        def update_related(field_name, model_class):
            if field_name in validated_data:
                data = validated_data.pop(field_name)
                # Clear existing related objects
                getattr(instance, field_name.replace('_data', '')).all().delete()
                # Create new ones
                for item in data:
                    model_class.objects.create(profile=instance, **item)

        # Update all nested relationships
        update_related('skills_data', Skill)
        update_related('projects_data', Project)
        update_related('experiences_data', Experience)
        update_related('educations_data', Education)
        update_related('certifications_data', Certification)
        update_related('awards_data', Award)

        return instance
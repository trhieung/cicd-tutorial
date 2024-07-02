import os
import sys
import django

# Add the project's directory to the Python path
django_project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(django_project_dir)

# Set the Django settings module manually
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CSC15004_project.settings")

# Import and configure Django
django.setup()

from final_lab.models import AmazonProductReviews

# Clear all existing data from the AmazonProductReviews model
AmazonProductReviews.objects.all().delete()
print("Cleared all existing data.")

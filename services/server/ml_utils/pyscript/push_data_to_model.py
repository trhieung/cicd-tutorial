import os
import sys
import json
import django

# Add the project's directory to the Python path
django_project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(django_project_dir)

# Set the Django settings module manually
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CSC15004_project.settings")

# Import and configure Django
django.setup()

from final_lab.models import AmazonProduct

def load_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as reader:
        for line in reader:
            data.append(json.loads(line))
    return data

# Path to the data file
data_file = os.path.join(django_project_dir, 'utils/data/data_2k.jsonl')

# Load the JSON data from the file
data = load_jsonl(data_file)

# Iterate over the data and create AmazonProduct objects
for item in data:
    review_text = item.get('reviewText')
    label = item.get('label')
    amazon_product = AmazonProduct(reviewText=review_text, label=label)
    amazon_product.save()

print("All data has been pushed to the model.")

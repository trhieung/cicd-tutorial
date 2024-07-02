import os
import sys
import django
import dotenv
import json

# Add the project's directory to the Python path
sys.path.append(os.getcwd())

dotenv.load_dotenv(os.path.join(os.getcwd(), '../../env/server/.env'))

# # Set the Django settings module manually
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.getenv("DJANGO_SETTINGS_MODULE"))

# Import and configure Django
django.setup()
#--------------------------------------------------------------------------

from transformer.models import AmazonProductReviews, AmazonLabels

def load_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as reader:
        for line in reader:
            data.append(json.loads(line))

    reviews = []
    for idx, item in enumerate(data):
        review_text = item.get('reviewText')
        label_id = item.get('label')

        # Get or create the AmazonLabels instance
        label, _ = AmazonLabels.objects.get_or_create(label=label_id)

        # Create the AmazonProductReviews instance
        review = AmazonProductReviews(label=label, reviewText=review_text)
        reviews.append(review)
        if idx %10 == 0: print(idx)

    # Bulk create the reviews
    AmazonProductReviews.objects.bulk_create(reviews)

# Path to the JSONL file
jsonl_path = os.path.join(os.getcwd(), 'ml_utils/data/data_10.jsonl')

# Load the JSONL data
load_jsonl(jsonl_path)


print("All data has been pushed to the model.")
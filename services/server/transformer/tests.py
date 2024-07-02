from django.test import TestCase

# Create your tests here.
import requests

BASE_URL = 'http://localhost:8000/'  # Replace with the actual base URL of the API

def get_labels():
    response = requests.get(f'{BASE_URL}labels/')
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_label(pk):
    response = requests.get(f'{BASE_URL}labels/{pk}/')
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def highlight_label(pk):
    response = requests.get(f'{BASE_URL}labels/{pk}/highlight/')
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def create_label(data):
    response = requests.post(f'{BASE_URL}labels/', json=data)
    if response.status_code == 201:
        return response.json()
    else:
        response.raise_for_status()

def update_label(pk, data):
    response = requests.put(f'{BASE_URL}labels/{pk}/', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def delete_label(pk):
    response = requests.delete(f'{BASE_URL}labels/{pk}/')
    if response.status_code == 204:
        return 'Label deleted successfully'
    else:
        response.raise_for_status()

# Example usage
if __name__ == '__main__':
    # List all labels
    labels = get_labels()
    print('Labels:', labels)
    
    # Get a specific label by ID
    label = get_label(1)
    print('Label 1:', label)
    
    # Highlight a specific label by ID
    highlighted_label = highlight_label(1)
    print('Highlighted Label 1:', highlighted_label)
    
    # Create a new label
    new_label = {
        'name': 'New Label',
        'description': 'This is a new label'
    }
    created_label = create_label(new_label)
    print('Created Label:', created_label)
    
    # Update an existing label
    updated_data = {
        'name': 'Updated Label',
        'description': 'This label has been updated'
    }
    updated_label = update_label(1, updated_data)
    print('Updated Label 1:', updated_label)
    
    # Delete a label
    delete_message = delete_label(1)
    print(delete_message)


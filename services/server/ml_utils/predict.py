# import numpy as np
import torch
# import torch.nn as nn
# from torch.utils.data import Dataset
# from torch.utils.data import DataLoader
# import torch.optim as optim
# import torch.nn.functional as F
# from tqdm import tqdm
from transformers import PreTrainedTokenizerBase
from transformers import AutoModelForSequenceClassification, AutoTokenizer
# from transformers import BertForSequenceClassification, BertTi=okenizer


EVAL_BATCH_SIZE = 16
MAX_LENGTH = 512 # MAX LENGTH OF INPUT STRING

label_dict = {
        0: 'Amazon Instant Video',
        1: 'Apps for Android',
        2: 'Automotive',
        3: 'Baby',
        4: 'Beauty',
        5: 'Books',
        6: 'CDs and Vinyl',
        7: 'Cell Phones and Accessories',
        8: 'Clothing Shoes and Jewelry',
        9: 'Digital Music',
        10: 'Electronics',
        11: 'Grocery and Gourmet Food',
        12: 'Health and Personal Care',
        13: 'Home and Kitchen',
        14: 'Kindle Store',
        15: 'Movies and TV',
        16: 'Musical Instruments',
        17: 'Office Products',
        18: 'Patio Lawn and Garden',
        19: 'Pet Supplies',
        20: 'Sports and Outdoors',
        21: 'Tools and Home Improvement',
        22: 'Toys and Games',
        23: 'Video Games'}

num_labels = len(label_dict)

# class AmazonProductDataset(Dataset):
#     def __init__(self, all_data: list, tokenizer: PreTrainedTokenizerBase, max_length: int = 512):
#         super(AmazonProductDataset, self).__init__()
        
#         self.all_data = all_data
#         self.tokenizer = tokenizer
#         self.max_length = max_length

#     def __getitem__(self, idx):
#         data_item = self.all_data[idx]
#         data_encoding = self.tokenizer(data_item["reviewText"], 
#                                        truncation=True,
#                                        max_length=self.max_length,
#                                        padding="max_length",
#                                        return_tensors="pt")

#         return {
#             "input_ids": data_encoding["input_ids"].flatten(),
#             "attention_mask": data_encoding["attention_mask"].flatten(),
#             "labels": torch.tensor(data_item["label"]).long(),
#         }

#     def __len__(self):
#         return len(self.all_data)
    

model_name = "nthieu/amazon-product-classifier-epoch-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
bert = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

@torch.no_grad()
def predict(model, input):
    model.eval()
    outputs = model(**input)
    
    # Get the predicted label
    predicted_label = torch.argmax(outputs.logits, dim=1).item()
    return predicted_label

def encoding_text(text: str, tokenizer: PreTrainedTokenizerBase):
    return tokenizer(text, 
                     truncation=True,
                     max_length=512,
                     padding="max_length",
                     return_tensors="pt")


"""
test_messages = [{
                    "reviewText": "No sugar, no GMO garbage, no fillers that come with store bought extracts. This stuff is just amazing. I use it in everything from baking to cooking and even as suggested in my coffee which is saying a lot because I normally do not care for flavored coffee! You cannot go wrong with this. I've ordered from this merchant before, customer satisfaction is their priority and service was quick, shipped right out with tracking even! I'll be buying from GLS Goods again! I won't use any other vanilla!",
                    "label": 11
                },
                {
                    "reviewText": "This is a very unique scent! It's deep and mysterious and light and floral at the same time. The deep purple bottle is so fitting for the scent- it's dusky, smoky (it doesn't smell like smoke, but it gives off that vibe), with a hint of feminine innocence. This is a hard scent to describe, one that invokes images rather than particular notes. I've not smelled anything like this anywhere else.",
                    "label": 4
                }]

data_0_encoding = tokenizer(test_messages[0]["reviewText"], 
                                       truncation=True,
                                       max_length=512,
                                       padding="max_length",
                                       return_tensors="pt")

data_1_encoding = encoding_text(test_messages[1]["reviewText"], tokenizer)

# print()
# print(predict(bert, data_1_encoding))
print(label_dict[predict(bert, data_0_encoding)])
print(label_dict[predict(bert, data_1_encoding)])

"""

#x = "The quality of the printer toner replacement was very good, but the life of the toner was not as it indicated for up to 1200 piece. I used it for less than two months, and the total less than one pack of 500 piece paper. Even every piece was double side print which was not, it was total less than 1000 piece life"
#y = encoding_text(x, tokenizer)

#print(label_dict[predict(bert, y)])

def get_predict(x):
    y = encoding_text(x, tokenizer)
    return label_dict[predict(bert,y)]


# def get_predict(x):
#     # y = encoding_text(x, tokenizer)
#     # return label_dict[predict(bert,y)]
#     return "ahihi"
import pandas as pd
from get_location import get_location_LLM
from get_real_time_data import get_real_time_data_final_process
from fuzzywuzzy import process
import requests
from PIL import Image
from io import BytesIO
import torch
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np


# Match input location with camera location
def match_location(search_location, camera_location_split):
    best_match = process.extractOne(search_location, camera_location_split)
    best_match_index = camera_location_split.index(best_match[0])
    print('The best match location is {}'.format(best_match))
    return best_match_index

# get camera link
def get_image(camera_data, best_match_index):
    camera_link = camera_data.iloc[best_match_index]['ImageLink']
    # print('The camera link is {}'.format(camera_link))
    # get image
    response = requests.get(camera_link)
    if response.status_code == 200:
        image_bytes = BytesIO(response.content)
        
        # use Pillow open image
        image = Image.open(image_bytes)
        image.show()
    else:
        print("Failed to get image! Please try again!")
    
    return image

def predict_image(image, classes):
    map_location=torch.device('cpu')
    finetuning_weights_path = "finetuning_model.pth"
    model = torch.load(finetuning_weights_path, map_location=map_location)
    model.eval()

    # from the machine learning model script
    mean=[0.485, 0.456, 0.406]
    std=[0.229, 0.224, 0.225]

    # load model
    model = torch.load(finetuning_weights_path, map_location=map_location)
    model.eval()

    # pre-processing the image
    transform = transforms.Compose([
        transforms.Resize((400, 600)),  # resize
        transforms.ToTensor(),
        transforms.Normalize(mean=mean, std=std),  # normalization
    ])

    # transform
    image_tensor = transform(image).unsqueeze(0)  

    # predict the image
    with torch.no_grad():
        output = model(image_tensor)
        pred_label = output.argmax(1).item()
    # print(classes[pred_label])
    return classes[pred_label] 

def final_process():
    search_location = get_location_LLM()
    camera_data, camera_location_list, camera_location_split = get_real_time_data_final_process()
    best_match_index = match_location(search_location, camera_location_split)
    image = get_image(camera_data, best_match_index)
    classes=['Empty', 'High', 'Low', 'Medium', 'Traffic Jam']
    res = predict_image(image, classes)
    # print(res)
    return res

if __name__ == "__main__":
    print(final_process())
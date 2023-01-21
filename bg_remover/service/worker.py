from rembg import remove
import requests

def remove_background(image_url):

    response = requests.get(image_url)
    output = remove(response.content)
    return output

    

# Dilling
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- D

```sh
127.0.0.1:8000
```


# AI-Hire-Test


- Prototyping NLP search with background removal

### Introduction

The company wants to launch NLP search with a new customer.
However, the product photo backgrounds vary greatly.
From past experience, you know that product photo background affects search results.
The company wants to build NLP search for fashion products, not for different photo backdrops.
You are tasked with building a prototype of an NLP search that is smart enough to ignore the product photo background, the model's hairstyle etc.
However, the company is in a bit of a hurry, so you're asked to produce the prototype quickly.
[You've been given a sample of the product photos to aid you in prototyping.](https://drive.google.com/file/d/1Vvr-fO1duXhrHCp3HUG04oSwcX75PqU1/view?usp=share_link)

## The task

1. Implement background removal for product photos
2. Build an NLP search engine with the product photos provided to you
3. Make both 1. and 2. accessible over HTTP via JSON
4. Create Dockerfiles we can use to deploy the HTTP services for both 1. and 2.

## Requirements

1. Background removal
    - Replace the background pixels with RGB value \#000000, keep the foreground as is.
    - Consider as background anything that is NOT the product being displayed in the photo, like trees, other people, buildings, the model's face or hair etc.
    - The background-removed image should have the same dimensions as the original image
    - Use the background-removed images when searching for products for similar images in 2.
2. NLP search engine
    - By NLP search, we mean: given a text query, find the products whose product images are most similar to the text query.
    - In the image folder provided to you, 1 folder = 1 product, where each product can have more than one product photo
    - Use the name of the image folder as the product name
    - When returning results from the NLP search engine, make sure each product will be show

3. HTTP services for 1. and 2.

- Both services should accept POST requests in JSON requests in
1. Background removal
    - Input: url - the URL of the image to be processed
    - Output: the image, in JPEG format, with its background removed
    - A command that could be used to test whether the service works: `curl -XPOST -H'content-type: application/json' -d'{"url":"https://eg.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/55/373622/1.jpg?2661"}' http://localhost:6000/ > output.jpg`
2. NLP search
    - Input: text - the text query to use for searching similar products, n - number of products to show
    - Output: list of n results, sorted by score in descending order, where each item has the form `{"product_name": <name of the product>,"url": <path to a product image>,"score": <similarity score of text query to product image>}`
        - Example output (list of 1 result only): `[{"product_name": "mink-tunic-allday-7856692", "url": "sample/mink-tunic-allday-7856692/z-gizli-patli-tesettur-gomlek-tesettur-tunik-vizon-allday-7856692-1.jpg", "score": 0.959}]`
- A higher score should indicate higher similarity between text query and product
- A command that could be used to test whether the service works: `curl -XPOST -H'content-type: application/json' -d'{"text": "pastel coloured tunic", "n": 5}' <http://localhost:6000/ > output.jpg`

1.  Docker
    - Make both of the services run internally on port 5000
    - Each service should run in a separate Docker container

## Problems ecountered

##### NLP image search engine
- 1. NLP image search engine result isn't very accurate. it returns random images along side the correct ones mostly.
- 2. struggled to dockerize the flask app because the NLP runs on torch and torchvision which was problematic to get a base image in docker to satisfy this requirement. So, will suggest to be able to test this Flask App...clone the repo and install the requirement.txt file


```sh
pip install image-searcher
```
```sh
pip install -r requirements.txt
```

##### background remover


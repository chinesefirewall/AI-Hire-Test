from image_searcher import Search
from flask import Flask, request, Blueprint, jsonify




searcher = Search(image_dir_path="/Users/shade/Documents/NLP/ImageSearcher/Data/", 
                  traverse=True, 
                  include_faces=False)

# Pythonic API
def image_search(input_query, number_of_related_product):

    # search.rank takes in the input query and and number of relation to return
    ranked_images = searcher.rank_images(input_query, n = number_of_related_product)
  
    return ranked_images


app = Flask(__name__)
app.config.from_object(__name__)

nlp_search_egine = Blueprint('nlp_search_egine', __name__)

@app.route('/')
def status():  # put application's code here
    return {"status": "Online"}

@nlp_search_egine.route('/api/search-engine', methods=['POST'])
def image_search_engine():

    text = request.json['text']
    number = request.json['number']
    holder_var = image_search(text,number)
    print(holder_var)
    return jsonify(holder_var)

app.register_blueprint(nlp_search_egine)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6000)
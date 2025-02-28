#imports
import json
import os 
from datetime import timedelta, datetime
from flask import Flask, render_template, request, jsonify, redirect, make_response , url_for, send_from_directory
#from flask_cors import CORS  not needed as per local testing


paignation_data = [
    {
      "card_title": "Card Title 1",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/cards.jpg",
      "card_url": "https://example.com/card1"
    },
    {
      "card_title": "Card Title 2",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/federated-learning-flow.png",
      "card_url": "https://example.com/card2"
    },
    {
      "card_title": "Card Title 3",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/image_1.png",
      "card_url": "https://example.com/card3"
    },
    {
      "card_title": "Card Title 1",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/cards.jpg",
      "card_url": "https://example.com/card1"
    },
    {
      "card_title": "Card Title 2",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/federated-learning-flow.png",
      "card_url": "https://example.com/card2"
    },
    {
      "card_title": "Card Title 3",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/image_1.png",
      "card_url": "https://example.com/card3"
    },
    {
      "card_title": "Card Title 1",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/chat-app-icon.png",
      "card_url": "https://example.com/card1"
    },
    {
      "card_title": "Card Title 2",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/federated-learning-flow.png",
      "card_url": "https://example.com/card2"
    },
    {
      "card_title": "Card Title 3",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/image_1.png",
      "card_url": "https://example.com/card3"
    },
    {
      "card_title": "Card Title 1",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/cards.jpg",
      "card_url": "https://example.com/card1"
    },
    {
      "card_title": "Card Title 2",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/federated-learning-flow.png",
      "card_url": "https://example.com/card2"
    },
    {
      "card_title": "Card Title 3",
      "card_para": "System design is a multidisciplinary field that encompasses various aspects of designing distributed systems.",
      "img_src": "../images/image_1.png",
      "card_url": "https://example.com/card3"
    }
  ]
  





app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/section/<section>")
def section(section):
    return jsonify(paignation_data)




if __name__ == '__main__':
    app.run(port=5000, debug=True)
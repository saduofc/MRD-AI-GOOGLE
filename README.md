# Google Search Chatbot

Simple Flask app chatbot that gets user questions, searches Google, scrapes top page summary and replies.

## Setup

1. Create Python virtual environment  
2. Install dependencies: `pip install -r requirements.txt`  
3. Run app: `python app.py`  
4. Open browser at `http://localhost:5000`

## Notes

- Make sure internet connection is working  
- This app scrapes web pages — some websites might block scraping  
- Simple summary by extracting paragraphs  
- No OpenAI API needed  

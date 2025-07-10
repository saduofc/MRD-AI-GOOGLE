from flask import Flask, render_template, request, jsonify
from googlesearch import search
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def google_search_summary(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    for url in search(query, num_results=1):
        try:
            page = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(page.content, "html.parser")
            paragraphs = soup.find_all('p')
            summary = ''
            for para in paragraphs:
                text = para.get_text().strip()
                if len(text) > 50:
                    summary += text + ' '
                if len(summary) > 400:
                    break
            if summary:
                return summary[:500] + "..."
        except:
            continue
    return "සමාවන්න, මට උත්තර ලබාදීමට නොහැක."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({"answer": "කරුණාකර ප්‍රශ්නයක් ඇතුළත් කරන්න."})
    answer = google_search_summary(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)

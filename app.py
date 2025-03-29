from flask import Flask, jsonify, request
import webpage_summarizer
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "Hello World!!!"
        return jsonify({"data": data})


@app.route("/summarize", methods=["POST"])
def summarize():
    page_url = request.json["page_url"]
    page_summary = webpage_summarizer.summarize_webpage(page_url)

    if page_summary != "":
        summary = {
            "page_url": page_url,
            "page_summary": page_summary
        }

        return jsonify(summary)
    return jsonify({
        "page_url": page_url,
        "error": "Page could not be summarized."
    }), 400
if __name__ == "__main__":
    app.run(debug=True)
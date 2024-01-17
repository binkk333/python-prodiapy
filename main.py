from flask import Flask,request,jsonify
from prodiapy import Prodia
prodia = Prodia(
    api_key="530bd4ab-3ac5-4048-8609-81e3864c70fa"
)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/api/text2img", methods=['GET', 'POST'])
def text2img():
    if request.method == 'POST':
        try:
            data = request.get_json()
            prompt = data.get('prompt', '')
            
            if not prompt:
                return jsonify({"error": "Prompt is missing"}), 400
            
            job = prodia.sd.generate(prompt=prompt)
            result = prodia.wait(job)
            
            return jsonify({
                "imageUrl": result.image_url
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Method not allowed"}), 405

@app.route('/test')
def test():
    if request.method == 'GET':
            job = prodia.sd.generate(prompt="a cute japan girl ")
            result = prodia.wait(job)
            print(result.image_url)
            return jsonify( {
                "imageUrl" : result.image_url
            })
    else:
        return jsonify (
            {
                "error": "can't text to image"
            }
        )


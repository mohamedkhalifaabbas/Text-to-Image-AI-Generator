from flask import Flask, render_template, request, send_file, jsonify
from io import BytesIO
import base64
import random
from model_loader import generate_image  


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"error": "Prompt is required."})

    try:
        img = generate_image(prompt)
        buf = BytesIO()
        img.save(buf, format="PNG")
        image_data = base64.b64encode(buf.getvalue()).decode("utf-8")
        return jsonify({"image": image_data})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/download")
def download_image():
    prompt = request.args.get("prompt", "image")
    steps = int(request.args.get("steps", 30))
    guidance = float(request.args.get("guidance", 7.5))
    seed = int(request.args.get("seed", random.randint(1, 1000000)))

    img = generate_image(prompt, steps=steps, guidance=guidance, seed=seed)
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png", as_attachment=True, download_name=f"generated_image_{seed}.png")


if __name__ == "__main__":
    app.run(debug=True)

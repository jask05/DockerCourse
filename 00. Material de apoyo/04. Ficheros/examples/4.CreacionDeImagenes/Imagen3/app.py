from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
	"http://www.gifbin.com/bin/072018/kitten-saved-after-getting-stuck-in-sink-hole.gif",
    	"http://www.gifbin.com/bin/102016/tn_puppy-pulls-ferret-away-from-food.gif",
	"http://www.gifbin.com/bin/022017/tn_dog-bites-girl-39-s-tongue.gif",
	"http://www.gifbin.com/bin/112016/tn_drying-a-golden-retriever.gif",
	"http://www.gifbin.com/bin/092016/tn_dog-jumps-in-huge-pile-of-leaves-to-save-kid.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

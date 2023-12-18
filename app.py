from flask import Flask,render_template,request
from PIL import Image
import matplotlib.pyplot as plt

app = Flask(__name__)
images_folder=r'images'
sign_language_dict={
    'A':'a.png',
    'B':'b.png',
    'C':'c.png',
    'D':'d.png',
    'E':'e.png',
    'F':'f.png',
    'H':'h.png',
    'G':'g.png',
    'H':'h.png',
    'I':'i.png',
    'J':'j.png',
    'K':'k.png',
    'L':'l.png',
    'M':'m.png',
    'N':'n.png',
    'O':'o.png',
    'P':'p.png',
    'Q':'q.png',
    'R':'r.png',
    'S':'s.png',
    'T':'t.png',
    'U':'u.png',
    'V':'v.png',
    'W':'w.png',
    'X':'x.png',
    'Y':'y.png',
    'Z':'z.png',
}
def text_to_sign(text):
    sign_language_images=[]
    for letter in text.upper():
        if letter in sign_language_dict:
            image_path=(images_folder+"\\"+sign_language_dict[letter])
            try:
                img=Image.open(image_path)
                sign_language_images.append(img)
            except FileNotFoundError:
                print("image not found for letter",letter)
    translated_images = sign_language_images
    if translated_images:
        plt.figure(figsize=(12, 4))
        total_width = sum(img.width for img in translated_images)
        max_height = max(img.height for img in translated_images)
        combined_image = Image.new('RGB', (total_width, max_height))
    
        x_offset = 0
        for img in translated_images:
            combined_image.paste(img, (x_offset, 0))
            x_offset += img.width
            
        combined_image.save("static\my.png")
        
@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/show",methods=["GET","POST"])
def show():
    if request.method=="POST":
     first=request.form.get("harsh")
     t=True
     text_to_sign(first)
     
     return render_template("index.html",t=t)
    return render_template("index.html")
if __name__=="__main__":
 app.run(debug=True,port=5001)
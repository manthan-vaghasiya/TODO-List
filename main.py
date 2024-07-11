from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
lists = []
id = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    global id, lists
    if request.method == 'POST':
        if request.form['text'] == "":
            flash("Please Enter Text")
        else:
            id+=1
            lists.append({id:request.form['text']})
            flash("Text Successfully Added")
    return render_template('index.html', lists=lists)

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def edit(id):
    global lists
    if request.method == 'POST':
        for text in lists:
            for t in text:
                if t == id:
                    text[t] = request.form['text']
                    return redirect('/')
    for text in lists:
        for t in text:
            if t == id:
                texts = text
    return render_template('edit.html', list=texts)

@app.route("/delete/<int:id>")
def delete(id):
    global lists
    print(len(lists))
    print(lists)
    for text in range(len(lists)):
        for t in lists[text]:
            if t == id:
                del lists[text]
                return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,render_template,request
from scrapper import(search_incruit)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword=request.args.get("ketword")
    print(keyword)
    jobs=search_incruit(keyword)
    print(jobs)
    return render_template("search.html",jobs=enumerate(jobs))#앞의 jobs는 search,html에서 쓸 변수




if __name__ == '__main__':
    app.run(debug=True)


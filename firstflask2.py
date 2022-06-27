from flask import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def odd_even():
    if request.method == "GET":
        return """
        下に整数を入力してくれよな！。簡単に奇数か偶数か判定できちゃうぜい！
        <form action="/" method="POST">
        <input name="num"></input>
        </form>"""
    else:
        try:
            return """
            {}は{}だな！
            <form action="/" method="POST">
            <input name="num"></input>
            </form>""".format(str(request.form["num"]), ["2で割りきれるから偶数", "2で割りきれねえぞ？！奇数"][int(request.form["num"]) % 2])
        except:
            return """
                    有効な入力じゃねえぞ！出直してこい！
                    <form action="/" method="POST">
                    <input name="num"></input>
                    </form>"""


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
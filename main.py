from flask import Flask, request


app = Flask("main")


@app.route("/calc")
def calc():
    numbers = request.args
    a = numbers.get("a")
    b = numbers.get("b")
    c = int(a) + int(b)
    return str(c)


app.run()
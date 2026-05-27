from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Pattern Matching Function
def pattern_match(txt, pat):

    n = len(txt)
    m = len(pat)

    positions = []

    for i in range(n - m + 1):

        if txt[i:i+m] == pat:
            positions.append(i)

    return positions


# Home Route
@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    execution_time = ""

    if request.method == "POST":

        txt = request.form["text"]
        pat = request.form["pattern"]

        start_time = time.time()

        result = pattern_match(txt, pat)

        end_time = time.time()

        execution_time = round((end_time - start_time), 6)

        if len(result) == 0:
            result = "Pattern Not Found"

    return render_template(
        "index.html",
        result=result,
        execution_time=execution_time
    )


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)


# Required for Vercel
app = app

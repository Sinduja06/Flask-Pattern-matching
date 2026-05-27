from flask import Flask, render_template, request
import time

app = Flask(__name__)

def function(txt, pat, m, n):

    for i in range(m - n + 1):

        if txt[i:n+i] == pat:
            return i

    return -1

@app.route('/', methods=['GET', 'POST'])

def home():

    result = ""
    execution_time = ""

    if request.method == 'POST':

        txt = request.form['text']
        pat = request.form['pattern']

        stime = time.time()

        pos = function(txt, pat, len(txt), len(pat))

        etime = time.time()

        result = pos
        execution_time = etime - stime

    return render_template(
        'index.html',
        result=result,
        execution_time=execution_time
    )

if __name__ == '__main__':
    app.run(debug=True)
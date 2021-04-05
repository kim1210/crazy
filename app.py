from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/ajax_test', methods=['GET', 'POST'])
def ajax_test():
    if request.method =='POST':        
        return redirect(url_for('success'))
    return render_template('ajax_test.html')

@app.route('/success', methods=['POST'])
def success():
    testdata = request.get_json()
    print(testdata)
    return render_template('success.html', testdata = testdata)

# @app.route('/success', methods=['GET', 'POST'])
# def success():
#     if request.method == 'POST':
#         testdata = request.get_json()
#         print(testdata)
#         return render_template('success.html', testdata=testdata)
#     testdata=request.get_json()
#     print(testdata)
#     return render_template('success.html', testdata=testdata)

app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import pprint

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/ajax_test', methods=['GET', 'POST'])
def ajax_test():
    # testdata = request.get_json()
    # print(testdata)
    if request.method =='POST': 
        testdata = request.get_json()
        print(testdata)
        print(testdata[0])
        # print('으아아아')
        # pprint.pprint(request)
        return redirect(url_for('success', testdata=testdata))
    return render_template('ajax_test.html')

# @app.route('/success', methods=['POST'])
# def success():
#     testdata = request.get_json()
#     print(testdata)
#     print(type(testdata))
#     return render_template('success.html', testdata = testdata)

@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        testdata = request.get_json()
        # pprint.pprint(request)
        print('post')
        print(testdata)
        print(testdata[0]['text'])
        return render_template('success.html', testdata=testdata)
    testdata=request.get_json()
    print(testdata)
    print('get')
    return render_template('success.html', testdata=testdata)

app.run(debug=True)
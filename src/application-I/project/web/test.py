
@app.route('/', methods=['GET'])
def hello():
    #with open('project/test_data.json', 'r') as f:
    #    data = f.read()
    #table = json2html.convert(data)
    #return table
    return render_template('index.html')

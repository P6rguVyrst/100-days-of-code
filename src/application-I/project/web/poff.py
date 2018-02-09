

@app.route('/poff', methods=['GET'])
def poff():
    with open('project/poff.json', 'r') as f:
        data = f.read()
    return data
    #table = json2html.convert(data)
    #return table
    #return render_template('index.html')



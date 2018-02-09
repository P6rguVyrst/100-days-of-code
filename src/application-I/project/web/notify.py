

@app.route('/notify', methods=['GET', 'POST'])
def listener():

    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        res = parse_request(data)
        if res.get('errors'):
            return jsonify(res), 415
        else:
            LOGGER.info(data)
            # Writing directly to file because could not get rsyslog to route socket messages to file.
            #with open("/var/log/100daysofcode.log", "a") as myfile:
            #    myfile.write(str(data) + '\n')

            return jsonify(res), 201
    else:
        return jsonify({'message': "POST me a message."}), 200



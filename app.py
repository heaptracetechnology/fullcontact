#!/usr/bin/env python

import os
import sys
import requests
from flask import Flask, request, jsonify


app = Flask(__name__)


def api(endpoint, data):
    res = requests.post(
        f'https://api.fullcontact.com/v3/{endpoint}.enrich',
        data=data,
        headers={
            'Authorization': f'Bearer {os.getenv("API_KEY")}',
            'User-Agent': os.getenv('USER_AGENT')
        }
    )

    try:
        res.raise_for_status()
    except:
        sys.stderr.write(res.text)
        raise
    else:
        # https://docs.fullcontact.com/#rate-limiting
        # TODO res.headers['X-Rate-Limit-Remaining']
        # TODO res.headers['X-Rate-Limit-Reset']
        # TODO res.headers['X-Rate-Limit']
        return res.json()


@app.route('/person', methods=['POST'])
def person():
    return jsonify(api('person', request.data))


@app.route('/company', methods=['POST'])
def company():
    return jsonify(api('company', request.data))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from zlasker import app

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=8000)

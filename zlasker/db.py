#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import sqlite3
from flask import g
from zlasker import app


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def create_table(drop=False):
    with app.app_context():
        db = get_db()
        if drop:
            db.execute('drop table if exists entries')
        with app.open_resource('schema.sql', mode='r') as f:
            db.executescript(f.read())
        db.commit()


def get_entries():
    cur = get_db().execute('select title, text from entries order by id desc')
    return cur.fetchall()


def add_entry(title, text):
    get_db().execute(
        'insert into entries (title, text) values (?, ?)', [title, text])
    get_db().commit()

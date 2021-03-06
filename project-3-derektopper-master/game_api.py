#!/usr/bin/env python
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"


@app.route("/purchase_a_sword")
def purchase_a_sword():
    purchase_sword_event = {'event_type': 'purchase_sword',
                           'description': 'upgrade sword strength',
                           'amount': '1'}
    log_to_kafka('events', purchase_sword_event)
    return "Sword Purchased!\n"

@app.route("/purchase_a_knife")
def purchase_a_knife():
    purchase_knife_event = {'event_type': 'purchase_knife',
                           'description': 'upgrade knife strength',
                           'amount': '1'}
    log_to_kafka('events', purchase_knife_event)
    return "Knife Purchased!\n"

@app.route("/purchase_armor")
def purchase_armor():
    purchase_armor_event = {'event_type': 'purchase_armor',
                           'description': 'upgrade armor strength',
                           'amount': '1'}
    log_to_kafka('events', purchase_armor_event)
    return "Armor Purchased!\n"

@app.route("/purchase_bow")
def purchase_bow():
    purchase_bow_event = {'event_type': 'purchase_bow',
                           'description': 'upgrade bow strength',
                           'amount': '1'}
    log_to_kafka('events', purchase_bow_event)
    return "Bow Purchased!\n"

@app.route("/purchase_arrow")
def purchase_arrow():
    purchase_arrow_event = {'event_type': 'purchase_arrow',
                           'description': 'upgrade arrow strength',
                           'amount': '1'}
    log_to_kafka('events', purchase_arrow_event)
    return "Arrow Purchased!\n"


@app.route("/join_guild")
def join_guild():
    join_guild_event = {'event_type': 'join_guild',
                        'description': 'joining a guild'}
    log_to_kafka('events', join_guild_event)
    return "Joined Guild!\n"



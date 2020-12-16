from flask import render_template, Blueprint, request, jsonify, current_app

homebp = Blueprint("homebp", __name__)


@homebp.route('/')
def report_index():
    # flash('You were successfully logged in')
    return render_template('index.html')


@homebp.route('/api/ping')
def ping():
    return jsonify({
        "ping": "Pong!",
        "ip": request.remote_addr,
        "router": request.path,
        "module": __name__,
        "version": "v1"
    })


@homebp.route('/api/v1')
def get_api():
    rules = []
    for rule in current_app.url_map.iter_rules():
        rules.append({
            "rule": rule.rule,
            "endpoint": rule.endpoint,
            "methods": str(rule.methods)
        })

    return jsonify({
        "msg": "apis",
        "rules": rules
    })

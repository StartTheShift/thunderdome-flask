thunderdome-flask
=================

Extension that helps integrate [thunderdome](https://github.com/StartTheShift/thunderdome) with Flask

Installation
============

This package is available via pip

    pip install thunderdome-flask

Usage
=====

This package allows you to register your vertices as flask converters so the
objects can loaded and passed in as parameters to your routes. For example:

```python
from flask import Flask
from myapp.models import Group, User
import thunderdome_flask

app = Flask(__name__)

# Register all available models as flask converters
thunderdome_flask.register_converters(app)

@app.route('/groups/<group:group_obj>', methods=['GET'])
def get_group(group_obj)
    group_obj.name = "Hello"
    group_obj.save()
    return jsonify(group_obj)
```

Now if you call the route the converters will automatically attempt to load
the vertex with the given id using the Vertex.get(...) method. So hitting the
route:

    /groups/33d6a58c-6bf1-41e5-a29b-6e5d0b067d50

Should change the name of the group to hello and return the jsonified object
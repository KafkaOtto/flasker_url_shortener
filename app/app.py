#!/usr/bin/env python3
from appconfig import app
from controller.url_controller import api

# register the api
app.register_blueprint(api)

if __name__ == '__main__':
    ''' run application '''
    app.run(debug=True, host='0.0.0.0', port=8000)
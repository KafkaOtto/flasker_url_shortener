#!/usr/bin/env python3
from appconfig import app
from controller.user_controller import user_api

# register the api
app.register_blueprint(user_api)

if __name__ == '__main__':
    ''' run application '''
    app.run(debug=True, host='0.0.0.0', port=8001)
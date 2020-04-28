from peppa_soc import rest_assoc
from peppa_soc import api, app
rest_assoc.api(api)

if __name__ == '__main__':
    app.run(debug=True, auto_reload=False)

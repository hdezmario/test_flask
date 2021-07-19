from typing import Set

from sqlalchemy.sql.expression import true
from apps import create_app

seting_modulo='config.desarrollo.Configuracion'

app = create_app(settings_module=seting_modulo)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
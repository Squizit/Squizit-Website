from flask_login import UserMixin
from remodel.helpers import create_tables, create_indexes
from remodel.models import Model


class User(Model, UserMixin):
    def get_id(self):
        return self['id']

create_tables()  # Remodel Table Creation
create_indexes()  # Remodel Relation Index Creation

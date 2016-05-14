from remodel.helpers import create_tables, create_indexes
from remodel.models import Model


class User(Model):
    def is_authenticated(self):
        return True

    def is_active(self):
        if 'active' in self:
            return self['active']

    def is_anonymous(self):
        return True

    def get_id(self):
        if 'uid' in self:
            return self['uid']

create_tables()  # Remodel Table Creation
create_indexes()  # Remodel Relation Index Creation

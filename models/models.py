from init import db, dt


class Customers(db.Model):
    __tablename__ = 'Customers'

    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(120), nullable=False, unique=True)
    added_date = db.Column(db.String(50), nullable=False)

    order = db.relationship('Orders', backref='order', uselist=False, cascade="all, delete, delete-orphan")

    def __init__(self, login_name):
        self.login_name = login_name
        self.added_date = dt.now().strftime('%m/%d/%Y %H:%M:%S')

    def get_info_dict(self):
        return {
            'id': self.id,
            'login_name': self.login_name,
            'added_date_TIMESTAMP': self.added_date
        }

    def to_dict(self):
        return {
            'login_name': self.login_name,
        }

    def get_relations(self):
        return {}

    def __repr__(self):
        return f'Customer({self.login_name}, {self.added_date})'


class Platformtypes(db.Model):
    __tablename__ = 'Platformtypes'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False, unique=True)

    platform = db.relationship('Platforms', backref='platform', uselist=False, cascade="all, delete, delete-orphan")

    def __init__(self, type):
        self.type = type

    def get_info_dict(self):
        return {
            'id': self.id,
            'type': self.type
        }

    def to_dict(self):
        return {
            'type': self.type
        }

    def get_relations(self):
        return {}

    def __repr__(self):
        return f'PlatformType({self.type})'


class Platforms(db.Model):
    __tablename__ = 'Platforms'

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('Platformtypes.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)

    order = db.relationship('Orders', backref='platform_order', uselist=False, cascade='all, delete, delete-orphan')

    def __init__(self, price, type_id):
        self.price = price
        self.type_id = type_id

    def get_info_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'type_id': self.type_id,
        }

    def to_dict(self):
        return {

            'price': self.price,
        }

    def get_relations(self):
        return {
            'Platformtypes': ['id'],
        }

    def __repr__(self):
        return f'Platform({self.price}, {self.type_id})'


class Orders(db.Model):
    __tablename__ = 'Orders'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    added_time_TIMESTAMP = db.Column(db.Integer, nullable=False)
    play_time = db.Column(db.Float, nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('Customers.id'), nullable=False)
    platform_id = db.Column(db.Integer, db.ForeignKey('Platforms.id'), nullable=False, unique=True)

    def __init__(self, play_time, customer_id, platform_id):
        self.price = 0
        self.added_time_TIMESTAMP = dt.timestamp(dt.now())
        self.play_time = play_time
        self.customer_id = customer_id
        self.platform_id = platform_id

    def get_info_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'added_time': self.added_time_TIMESTAMP,
            'play_time': self.play_time,
            'customer_id': self.customer_id,
            'platform_id': self.platform_id
        }

    def to_dict(self):
        return {
            'play_time': self.play_time,
        }

    def get_relations(self):
        return {
            'Customers': ['id'],
            'Platforms': ['id']
        }

    def __repr__(self):
        return f'Order({self.play_time}, {self.customer_id}, {self.platform_id}, {self.price})'


MODELS = {
    'Customers': Customers,
    'Orders': Orders,
    'Platformtypes': Platformtypes,
    'Platforms': Platforms,
}

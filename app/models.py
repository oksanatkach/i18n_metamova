from app import app, db 


class Contact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)


	def __repr__(self):
		return '<Email: {}>'.format(self.email)

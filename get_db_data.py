import xlsxwriter
from app.models import Contact

def get_data():
	users = Contact.query.all()
	get_users = [user.__dict__["email"] for user in users]
	
	workbook = xlsxwriter.Workbook('email_db.xlsx')
	worksheet = workbook.add_worksheet()

	row = 0 
	for email in get_users:
		worksheet.write(row, 0, email)
		row += 1

	workbook.close()

if __name__ == '__main__':
	get_data()

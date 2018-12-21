from openpyxl import *
import sys
from user import User
class ExcelManager:
	"""docstring for ExcelManager"""
	def __init__(self, filename):
		super().__init__()
		self.filename = filename
		try:
			self.workbook = load_workbook(filename)
			first_sheet_name = self.workbook.sheetnames[0]
			self.first_sheet = self.workbook[first_sheet_name]			
		except Error as err:
			self.first_sheet = None
			print("Error loading workbook: {0}".format(err))
	def fill_data_to_first_sheet(self, users):
		"""Header"""			
		self.first_sheet['A1'] = 'Tên'
		self.first_sheet['B1'] = 'Email'
		self.first_sheet['C1'] = 'Điện thoại'
		self.first_sheet['D1'] = 'Wesite'
		row_number = 2
		for user in users:
			# import pdb
			# pdb.set_trace()
			self.first_sheet['A{}'.format(row_number)] = user.name
			self.first_sheet['B{}'.format(row_number)] = user.email
			self.first_sheet['C{}'.format(row_number)] = user.phone
			self.first_sheet['D{}'.format(row_number)] = user.website
			self.first_sheet['E{}'.format(row_number)] = '=CONCATENATE(C{},D{})'.format(row_number, row_number)
			row_number = row_number + 1			
		self.workbook.save(self.filename)

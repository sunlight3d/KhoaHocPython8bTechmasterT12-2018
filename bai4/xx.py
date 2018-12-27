from openpyxl import *
import sys
from user import User
class ExcelManager:
	def __init__(self, filename):
		super().__init__()
		self.filename = filename
		try:
			self.workbook = load_workbook(filename)
			first_sheet_name = self.workbook.sheetnames[0]
			self.first_sheet = self.workbook[first_sheet_name]
			print('Load file excel thanh cong')
		except Exception as loi:
			self.first_sheet = None
			print("Error loading workbook: {0}".format(loi))
	def fill_data_to_first_sheet(self, users):
		"""Header"""			
		self.first_sheet['A1'] = 'Tên'
from openpyxl import *
import sys

class ExcelManager:
	"""docstring for ExcelManager"""
	def __init__(self, filename):
		super().__init__()
		self.filename = filename
		try:
			self.workbook = load_workbook(filename)
			first_sheet = self.workbook.sheetnames[0]
		except Error as err:
			print("Error loading workbook: {0}".format(err))
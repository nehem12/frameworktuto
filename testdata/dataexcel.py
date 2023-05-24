from openpyxl import Workbook

flightdata = Workbook()
firstsheet = flightdata.active
firstsheet['A1'] = "Departure city"
firstsheet['B1'] = "Destination city"
firstsheet['A2'] = "Kolkata"
firstsheet['B2'] = "Pune"
firstsheet['A3'] = "Chennai"
firstsheet['B3'] = "Mumbai"
flightdata.save(filename="flightcity.xlsx")


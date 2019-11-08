import requests
from bs4 import BeautifulSoup

def main():
	id = input('Enter your id: ')
	params = {'__VIEWSTATE':'/wEPDwUJNTk3NTAxNTk0D2QWAmYPZBYCAgIPZBYEAgEPZBYoAgUPDxYCHgdWaXNpYmxlaGRkAgcPDxYCHwBoZGQCCQ8PFgIfAGhkZAILDw8WAh8AaGRkAg0PDxYCHwBoZGQCDw8PFgIfAGhkZAIRDw8WAh8AaGRkAhMPDxYCHwBoZGQCFQ8PFgIfAGhkZAIXDw8WAh8AaGRkAhkPDxYCHwBoZGQCGw8PFgIfAGhkZAIdDw8WAh8AaGRkAh8PPCsACwBkAiEPDxYCHwBoZGQCIw88KwALAGQCJQ8PFgIfAGhkZAInDzwrAAsAZAIpDw8WAh8AaGRkAisPPCsACwBkAgMPZBYCAgEPDxYCHgRUZXh0BQQwMDU5ZGRkdCPU1VONldQZiXFsDNuHTGIVz54=',
		  '__EVENTVALIDATION':'/wEWAwK5jILLBgL02Yi2DgLWlvWyA6e1sSs+2YzVuOZXmErw6hClycA0','ctl00$CPHmaster$txtMemcd':id,'ctl00$CPHmaster$btnsearch':'Search Member'}
	req = requests.post('http://webopac.cit.ac.in/memberstatus.aspx', data=params)
	parse = BeautifulSoup(req.text, 'lxml')
	#print(parse)
	member_name = parse.find('span', id='ctl00_CPHmaster_lblmemname').text.strip()
	#print(member_name)
	member_code = parse.find('span', id='ctl00_CPHmaster_lblmemcd').text.strip()
	member_dept = parse.find('span', id='ctl00_CPHmaster_lbldept').text.strip()
	#print(member_name, member_code, member_dept)
	member_cat = parse.find('span', id='ctl00_CPHmaster_lblcat').text.strip()
	member_dues = parse.find('span',id="ctl00_CPHmaster_lbldue").text.strip()
	member_book_count = parse.find('span', id='ctl00_CPHmaster_lblissued').text.strip()
	#print(member_cat, member_due, member_book_count)
	items = parse.find('table', id='ctl00_CPHmaster_DgIssued')
	#print(items)
	rows = items.find_all('tr')[1:]
	#print(rows)
	for row in rows:
   		cols = row.find_all('td')
   		for col in cols:
      			print(col.text)
   		print('')


if __name__=='__main__':
	main()

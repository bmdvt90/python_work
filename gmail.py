#test for sending email
def gmail(pwd):
	import smtplib
	smtpObj = smtplib.SMTP('smtp.gmail.com',587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('bmattdillard@gmail.com',pwd)
	smtpObj.sendmail('bmattdillard@gmail.com','bmattdillard@dtsfederal.com','Subject:Test from Python.\n this is a test of the emergency broadcast system')
	smtpObj.quit()
#end

#test twilio text
def text(pwd):
	from twilio.rest import Client
	accountSID = 'AC2893a2ff142057ee075027d3b97033e2'
	authToken = pwd
	client = Client(accountSID, authToken)
	
	call = client.calls.create(
		to='7033464041',
		from_='7039400674',
		body='Take Cover!!')


#gmail('BMD_0798')
text('7b5792b924898de59be3332f80e088a2')

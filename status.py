import urllib.request
import urllib.error

code = {
	"None" : "Input a valid HTTP URL",
	200 : "OK",
	201 : "The POST command was a success!",
	202 : "Request for processing accepted but it may be disallowed when processing actually takes place.",
	203 : "The returned metainformation is not a definitive set of the object from a" + 
	" server with a copy of the object, but is from a private overlaid web.",
	204 : "No information to send back from the server. Please stay in the same document"+
	" view to allow input for scripts without changing the document at the same time.",
	400 : "Either the request had bad syntax or is inherently impossible to be satisfied",
	401 : "Retry the request with a suitable Authorization header.",
	402 : "Retry the request with a suitable ChargeTo header.",
	403 : "The request is for something forbidden and unfortunately, authorization will not help.",
	404 : "Nothing that matches the URI was found by the server.",
	500 : "Unexpected condition encountered by the server is preventing it from fulfilling"+
	" the request.",
	501 : "The server does not support the facility required.",
	502 : "The server cannot process the request due to a high load but the"+
	" good news is that this is a temporary condition which maybe alleviated at other times!",
	503 : "The respose from the other service which the server tried to access did not return"+
	" within a time that the gateway was prepared to wait.",
	301 : "The data requested has been assigned a new URI and the change is permanent.",
	302 : "The data requested actually resides under a different URL, however, the redirection may be "+
	"altered on occasion as for 'Forward'.",
	303 : "You should try another network address.",
	304 : "The server did not send the document body since the document has not been modified "+
	"since the date and time specified in If-Modified-Since field."
	}

url = input("Enter URL")
try :
	link = urllib.request.urlopen(url)
	message = link.getcode()
	for key in code.keys():
		if message == key :
			print (code[key])
			break
	else:
		print("Unidentified code returned.")
except urllib.error.HTTPError as err :
	for key in code.keys():
		if err.code == key :
			print(code[key])
			break
	else:
		raise


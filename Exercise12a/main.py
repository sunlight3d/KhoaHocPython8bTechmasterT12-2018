from http_request import HTTPRequest
http_request = HTTPRequest('https://www.vpbank.com.vn/vpb-exchange-rates')
http_request.get_response()
http_request.get_objects_from_text()

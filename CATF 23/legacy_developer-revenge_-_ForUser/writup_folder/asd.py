import jwt
import datetime

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except IOError:
        print(f"Error: Unable to read the file '{file_path}'.")
        return None

token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTkyLCJleHAiOjE2OTA1MTEwNTcsImlzcyI6Ii9hcGkvc2VjcmV0cy9wdWJsaWNrZXkifQ.BhsmaykFuOVqSQ6I1Gmwz0RpUKDSd1fXYBDulj5ELrapzsw2QFP0xVCn1bNwiMgKdTE_ucaZQy6RXw3U2sFv_nEHhu8QuB2aoxYA7slMh8hiSX1k9ypPJmUzUD6Ywc0ieZDTH-rX3FZkm24jPSv8Z6iD8P9nn2e_ywWawQ46b1ASuYn34mrG6TJIwV-AZzK1RdqX8EjRYMecNifrEJMu2wSJJXLkvFfH79McrZsBcbdiTnD4116-E32DVIM_jgQe54cWo02DppjSE1xnPX_wlcA1ylnsx2NdyT2AQqy5B_CJ4K-Au1CbfiN1ywyenX_vyExo20Nr6_AMh8nm_MfvNlDl7a8lsS6kigmV_CvAcB2EOBaHM24gyGRv914R-JHg8XTko2gPIoFP-UdTIrHt9tl_ync74Nw8GhhD-pGjguGmtbO4ACpCr7OU6zdU91A0QYUbIe8RJ0cKxA6G3DUyEcOLFw8shDr3JxcLLFjoyZuVRMXENZUlooIaWWi-1uwWrLSGGFYqoelNQ_U6p9dhgASepLndY0lqoXrsQsE0O_0ZWVhjpKiHrSATxGxKtMGP3KY8EtTCznzQzhexg2jyoMRgD3uaZdtQ03vlv9d4BfRkzuMrZmPXtuF53FSbzGJsE5KD_L6oOetF5caG7-SSIHegblZ01CtuUvN_VR-ENpw'
publickey = read_file('./publickey.pem' )
keypath = '/api/secrets/publickey'

newToken = jwt.encode(
    {'id': 1, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=90)
    , 'iss': keypath}
    , publickey,
    algorithm="RS256")  
print(newToken)
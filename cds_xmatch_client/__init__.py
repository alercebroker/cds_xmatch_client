import io
import pandas as pd
import requests

class XmatchClient:

    def __init__(self,url):
        self.url = url

    def execute(self,df: pd.core.frame.DataFrame,
        	        extcatalog: str,
		            distmaxarcsec: int = 1) -> (list, list):

        subset = df[ ['ra','dec','oid']]
        subset.rename(columns={ 'ra' : 'ra_in', 'dec' : 'dec_in' }, inplace=True)
        s = io.StringIO()
        subset.to_csv(s)

        table_str = s.getvalue()
        # Send the request!
        r = requests.post('http://cdsxmatch.u-strasbg.fr/xmatch/api/v1/sync',
		data={
		    'request': 'xmatch',
		    'distMaxArcsec': distmaxarcsec,
		    'selection': 'best',
		    'RESPONSEFORMAT': 'csv',
		    'cat2': extcatalog,
		    'colRA1': 'ra_in',
		    'colDec1': 'dec_in'},
		files={'cat1': table_str})

        bytes_response = io.BytesIO(r.content)
        result = pd.read_csv(bytes_response)

        return result

import io
import pandas as pd
import requests

CATALOG_MAP = {
		'allwise' : 'vizier:II/328/allwise',
		'gaia-dr2' : 'vizier:I/345/gaia2',
		'sdss-dr12' : 'vizier:V/147/sdss12'
}

class XmatchClient:

	def execute(self,df: pd.core.frame.DataFrame, extcatalog: str, distmaxarcsec: int = 1) -> (pd.core.frame.DataFrame):

		extcatalog = CATALOG_MAP[extcatalog]
		# Encode input
		subset = df[ ['ra','dec','oid']]
		subset.rename(columns={ 'ra' : 'ra_in', 'dec' : 'dec_in' }, inplace=True)
		s = io.StringIO()
		subset.to_csv(s)
		table_str = s.getvalue()

		# Send the request
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

		# Decode output
		print(r.text)
		bytes_response = io.BytesIO(r.content)
		result = pd.read_csv(bytes_response)

		return result

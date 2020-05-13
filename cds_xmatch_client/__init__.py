import io
import sys
import pandas as pd
import requests
import json
import pkg_resources

#catalog alias
input_path = pkg_resources.resource_filename('cds_xmatch_client','data/catalog_alias.json')
with open(input_path) as catalogs_file:
	CATALOG_MAP = json.load(catalogs_file)

class XmatchClient:

	def execute(self,df: pd.core.frame.DataFrame, extcatalog: str, selection: str, distmaxarcsec: int = 1) -> (pd.core.frame.DataFrame):

		try:
			#catalog alias
			if extcatalog in CATALOG_MAP:
				extcatalog = CATALOG_MAP[extcatalog]

			# Encode input
			new_columns = {}
			for c in df.columns:
				new_columns[c]="%s_in"%(c)
			df.rename(columns=new_columns, inplace=True)
			s = io.StringIO()
			df.to_csv(s)
			table_str = s.getvalue()

			# Send the request
			r = requests.post('http://cdsxmatch.u-strasbg.fr/xmatch/api/v1/sync',
			data={
			    'request': 'xmatch',
			    'distMaxArcsec': distmaxarcsec,
			    'selection': selection,
			    'RESPONSEFORMAT': 'csv',
			    'cat2': extcatalog,
			    'colRA1': 'ra_in',
			    'colDec1': 'dec_in'},
			files={'cat1': table_str})

			# Decode output
			bytes_response = io.BytesIO(r.content)
			result = pd.read_csv(bytes_response)
		except Exception as exception:
			sys.stderr.write( "Request to CDS xmatch failed: %s \n"%(exception) )
			raise exception

		return result

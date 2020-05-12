# CDS Xmatch Client

This repository contains a simple Python's client to the CDS XMatch API inspired in Fink's Broker implementation: https://github.com/astrolabsoftware/fink-broker developed by Julien Peloton.

* **Installation:**  `pip3 install git+https://github.com/alercebroker/cds_xmatch_client.git`

* **Usage:** This client esentially wraps the CDS Xmatch API to interact with Pandas DataFrames to handle catalogs.
  
  * **Coding** You can use it in your Python code:

    ```python
    import pandas as pd
    from cds_xmatch_client import XmatchClient

    client = XmatchClient()
    input  = pd.read_csv( some_input_path )
    catalog  = 'allwise'
    radius = 1
    output = client.xmatch(input,catalog,radius)
    ```
    
  * **Running scrìpt** Or you can run this script directly:
    
    ```bash
    cds_xmatch --input catalog.csv --catalog allwise --radius 1 --output result.csv
    ```
    
    ```bash
    cds_xmatch --help 

	usage: cdsxmatch [-h] [--input I] [--output O] [--catalog C]
			 [--radius R]

	Request CDS Xmatch API interacting with Pandas DataFrames

	optional arguments:
	  -h, --help          show this help message and exit
	  --input I           Path of input catalog dataframe
	  --output O          Path of result dataframe
	  --catalog C         Catalog name: allwise,gaia-dr2,sdss-dr7
	  --radius            R  Radius in arcseconds
    ```
  

# CDS Xmatch Client

This repository contains a simple Python's client to the [CDS XMatch API](http://cdsxmatch.u-strasbg.fr/xmatch/doc/) inspired in [Fink's Broker implementation](https://github.com/astrolabsoftware/fink-broker) developed by Julien Peloton.

* **Installation:**  `pip3 install git+https://github.com/alercebroker/cds_xmatch_client.git`

* **Usage:** This client wraps the CDS Xmatch API to interact with Pandas DataFrames and Astropy VOTables.
  
  * **Coding** You can use it in your Python code:

    ```python
    
    #CLIENT
    
    from cds_xmatch_client import XmatchClient
    client = XmatchClient()
    
    #PARAMS
    
    catalog_alias  = 'gaia-dr2'
    columns  = [ 'pmra', 'pmrdec' ]
    radius  = 2
    selection  = 'best'
    
    #INPUT: Pandas DataFrame / OUTPUT: Astropy VOTable
    
    import pandas as pd
    input_path = 'catalog.csv'
    input_type = 'pandas'
    df   = pd.read_csv(input_path)
    output_type = 'astropy'
    output = client.execute( 
    				df,
				input_type,
				catalog_alias,
				columns,
				selection,
				output_type,
				radius
    )
    
    #INPUT: Astropy VOTable / OUTPUT: Pandas DataFrame
    
    from astropy.table import Table
    input_path = 'catalog.xml'
    input_type = 'astropy'
    table = Table.read(input_path)
    output_type = 'pandas'
    output = client.execute(
    				table,
				input_type,
				catalog_alias,
				columns,
				selection,
				output_type,
				radius
    )
    ```
    
  * **Running scrìpt** Or you can run this script directly:
    
    ```
   	usage: cdsxmatch [-h] --input PATH --input_format FORMAT --output PATH
                 --output_format FORMAT --catalog NAME
                 [--catalog_columns COLS] [--radius R] [--selection S]

	Request CDS Xmatch API interacting with Pandas DataFrames

	optional arguments:
  	-h, --help            show this help message and exit
  	--input PATH          Path of input catalog
  	--input_format FORMAT
                        Input catalog format
  	--output PATH         Path of output result
  	--output_format FORMAT
                        Output format
  	--catalog NAME        Catalog name: an alias or a vizier identifier
  	--catalog_columns COLS
                        Columns selected from catalog
  	--radius R            Radius in arcseconds, up to 180
  	--selection S         Select between posible matches: best, all
    ```
    
 * **Catalogs** For a complete list of catalogs please search [Vizier's catalogs](https://vizier.u-strasbg.fr/viz-bin/VizieR). For convenience you can also use one of the aliases defined in [catalog_alias.json](https://github.com/alercebroker/cds_xmatch_client/blob/master/cds_xmatch_client/data/catalog_alias.json).
 
 * **Limitations** According to [CDS Xmatch API limitations](http://cdsxmatch.u-strasbg.fr/xmatch/doc/API-limitations.html)
  

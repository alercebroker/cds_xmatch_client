# CDS Xmatch Client

This repository contains a Python's client to the CDS XMatch API. 

* **Installation**  `pip3 install cds_xmatch_client`

* **Usage** 

This client esentially wraps the CDS Xmatch API to be able to interact with Pandas DataFrames to handle catalogs.
  
  * **Coding**
    You can use it in your Python code:

```
import pandas as pd
from cds_xmatch_client import Client

client = Client()
input  = pd-read_csv( some_input_path )
catalog_name  = 'allwise'
radius_arcsec = 1
output = client.xmatch(input,catalog_name,radius_arcsec)
```
  * **Running scrìpt**
    or directly by means of a script
    
    ```cds_xmatch --input catalog.csv --catalog allwise --radius 1 --output result.csv```


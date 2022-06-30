# ERP

## Database 数据库


| Sales | Type | Relation|
| --- | --- | -- |
| sales_id | Integer |
| customer_id | Integer | From Table "Customer" |
| term | String |
| date  |DateTime	  |  auto_now_add|
| start_time| DateTime|
| finish_time| DateTime|
| customer_po_id | String |
| product_id | Integer | From Table "Product"
| description | String |
| quantity | Decimal |
| unit_price | Decimal|
 
| Customer |Type   |Relation  |
| --- | --- | -- |
|customer_id |Integer   |  |
|customer_name  | String  |  |
|address  |String    |  |
|term  | String   |  |
|emali| Email |  |
|phone1  | Integer  |  |
|phone2  | Integer |  |

| Product|Type   |Relation  |
| --- | --- | -- |
|product_id|  Integer  |  |
|process_id | Integer   |  |
|bom_id |String    |  |
|date  |DateTime	  |  auto_now_add|
|quantity | Integer   |  |
|product_type  | String     |  |
|start_time  |DateTime    |  |
|finish_time |DateTime    |  |

| Product Material|Type   |Relation  |
| --- | --- | -- |
|product_id| Integer    |  |
|material_id| Integer    | From Table "Material " |
|usage| String     |  |

|Material|Type   |Relation  |
| --- | --- | -- |
|material_id| Integer     |  |
|grade| String      |  |
|size| String      |  |
|usage| String      |  |
|quantity|Integer      |  |

|Material Loration|Type   |Relation  |
| --- | --- | -- |
|shelf_id| Integer     |  |
|material_id| Integer     | From Table "Material " |
|quantity| Integer     |  |

|Supplier|Type   |Relation  |
| --- | --- | -- |
|supplier_id| Integer      |  |
|supplier_name| String       |  |
|address| String       |  |
|term| String       |  |
|email|Email   |  |
|phone1|Integer        |  |
|phone2|Integer        |  |

|Material Supplier|Type   |Relation  |
| --- | --- | -- |
|part_no| String        |  |
|supplier|String         |  |

|Process|Type   |Relation  |
| --- | --- | -- |
|product_id|  Integer        |  From Table "Product "|
|product_name| String          |  |
|type| String          |  |
|machine_id|Integer          |  |
|quantity|Integer         |  |
|term|String           |  |

|Machine|Type   |Relation  |
| --- | --- | -- |
|machine_id|Integer          |  |
|machine_name|String            |  |

|Product Good|Type   |Relation  |
| --- | --- | -- |
|goodbatch_id|Integer          |  |
|product_id|Integer          | From Table "Product" |
|customer_id|Integer          |From Table "Customer" |
|type|String            |  |
|quantity| Integer         |  |
|term|String            |  |
|date|DateTime	  |  auto_now_add|
|machine_id|Integer          |  |
|material|String            |  |

|Product Reject|Type   |Relation  |
| --- | --- | -- |
|rejectbatch_id| Integer         |  |
|product_id| Integer         | From Table "Product " |
|product_name|String  | |
|type|String            |  |
|quantity| Integer         |  |
|date|DateTime	  |  auto_now_add|
|machine_id|Integer          |  |

|Product Reject|Type   |Relation  |
| --- | --- | -- |
|rejectbatch_id| Integer         |  |
|product_id| Integer         | From Table "Product " |
|product_name|String  | |
|type|String            |  |
|quantity| Integer         |  |
|date|DateTime	  |  auto_now_add|
|machine_id|Integer          |  |

|BOM|Type   |Relation  |
| --- | --- | -- |
|bom_id| String  |  |
|product_id| String  | |
|material_id|String  | |
|usage|String            |  |
|remarks| String  |  |

|Delivery|Type   |Relation  |
| --- | --- | -- |
|sales_id| String  |  |
|sales_name| String  | |
|custiomer_id|String  | |
|product_id|String            |  |
|product_name| String  |  |
|quantity|String  	  |  |
|unitprice|String  |  |
|term|String  |  |
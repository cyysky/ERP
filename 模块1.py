
 Sales_Order#销售
    SalesOrderID
    CustomerID 
    customer_name
    term
    customer_po_id
    ProductID 
    description
    quantity
    unit_price 
    date
    start_time
    finish_time
    
 Customer#顾客
    CustomerID
    customer_name 
    address_ship
    address_sold 
    address_bill
    term
    email =
    phone1
    phone2
    
 Project_Sales_Item#项目
    ProjectSalesItemID
    project_name
    SalesOrderID
    CustomerID
    customerpart_id
    ProductID
    product_name
    quantity
    unitprice
    project_datenew
    term
    start_time 
    finish_time
    DeliveryID
    DeliveryDatetime
    
 Process#进程号
    ProcessID 
    process_name
    ResourceID
    ProjectSalesItemID
    ProductID
    process_tooling new
    start_time
    remarks
    
 BOM#物料清单
    BOMID
    ProductID 
    product_name 
    MaterialID 
    material_name 
    part_number 
    describe 
    quantity 
    UOM 
    usage 

 Material#材料
    MaterialID
    material_name
    MaterialSupplierID
    material_supplier_name
    measure_unit
    tybe
    Form
    thickness
    width
    length
    pltch
    default_stock_locatiuon
    usage
    quantity
    unit_price
    

      
 Material_Stock#材料库存
    MaterialStockID
    MaterialID 
    material_name
    material_location_id
    shelf_id
    quantity
    

 Require#要求 材料 
    RequireID
    MaterialID 
    material_name 
    ProjectSalesItemID 
    project_name 
    MaterialSupplierID 
    material_supplier_name 
    quantity 


 Purchase#交易的记录
    PurchaseID
    purchase_name 
    RequireID 
    deliver_date 
    MaterialID 
    material_name 
    quantity 
    unit_price 
    discount 
    total_MYR 
    remarks 
    MaterialSupplierID 

 Material_Supplier#材料供应商(交易信息)
    MaterialSupplierID
    SupplierID 
    MaterialID 
    material_name 
    quantity 
    remarks 
    
 Supplier#供应商()
    SupplierID
    supplier_name
    supplier_type
    address
    term
    email
    phone1
    phone2
    
 Material_Receive#收到材料
    MaterialReceiveID
    MaterialID 
    SupplierID 
    grade 
    size 
    usage 
    quantity 
    remarks 


 Resource#资源
    ResourceID
  
 Machine#机器
    MachineID
    machine_name
    unit_price
       
 Product#产品
    ProductID
    product_name
    product_group
    product_tooling
    product_unit
    materil_id
    material_usage
    ProjectSalesItemID
    BOMID
    date
    quantity 
    product_type
    start_time
    finish_time
    unit_price
        
 Product_Material#产品材质
    ProductID
    MaterialID
    usage
                
 Product_Good#产品好
    GoodbatchID
    ProductID
    product_name
    CustomerID
    MaterialID
    type 
    quantity
    term
    date
    
 Product_Reject#产品不合格
    RejectbatchID
    ProductID
    product_name
    MaterialID
    type
    quantity
    date
           
 Packaging#包装产品
    PackagingID
    packaging_name 
    packaging_unit 
    packaging_type 
    size
    heigh 
    width 
    length 
    model
    packaging_location  
    quantity  
    product_company 
    defaul_stock_location 

 Delivery#送货
    DeliveryID
    SalesOrderID
    sales_name
    CustomerID
    ProductID
    product_name
    quantity
    unitprice
    term
    DeliveryDatetime
    date

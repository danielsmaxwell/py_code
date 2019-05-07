
def qry_args (*args, **kw_args):

    """ 
    qry_args (field_name,... qry_parms,...)
    
    This functions returns an Oracle SQL select statement, using the field
    name(s) and query parameters provided by the caller.  The calling program 
    must provide at least one field_name.  As well, it must specify the table 
    or view to be queried in one of the qry_parms keyword/value pairs.  
     
    Here are some ways in which this function can be called:
    
    rtn = qry_args ('name', 'dept', table='employee') 
    rtn = qry_args ('name', table='employee', limiter='emp_id < 79654')  
    
    Possible keyword values: limiter (limit the result set), 
                               table (the table to query), 
                                view (the view to query). 
                                
    A return value of -1 (FAILURE) indicates that an error was encountered.
    """
    
    FAILURE = -1 
    
    table_found = False
    
    # Validate arguments and return FAILURE if any are missing
    
    assert len (args) > 0, 'No field name provided in qry_args()!'
    assert len (kw_args) > 0, 'No keyword/value pairs provided in qry_args()!'
    
      
    if len (args) == 0:                 
        print ('Argument Missing: No field names provided for qry_args()!')
        return FAILURE
         
    if len (kw_args) == 0:
        print ('Argument Missing: No keyword/value pairs provided for qry_args()!')
        return FAILURE
  
    for a in args:                      # Print argument(s)
        print ('Argument: ', a)         
    
    for (k, v) in kw_args.items():      # Print keyword/value pair(s)
        if k.lower() == 'view' or k.lower() == 'table':
            table_name  = v.lower() 
            table_found = True
            
        print (k, '=', v)              
    
    if table_found == False:            # Caller failed to provide a table or view name
        print ('Argument Missing: No table or view provided for qry_args()!')
        return FAILURE
 
# -----------------------------------------------------------------------------   

rtn = qry_args ('name', view='employee')

# rtn = qry_args ('name', view='employee')

if (rtn == FAILURE):
    print ('Call to qry_args() failed')
    

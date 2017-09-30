def param_test (a_float, a_int, a_string, *a_list, **a_dict): 

    """ 
    param_test ()
    
    This function illustrates best practices for validating data passed to a
    function.  A list of the most common Python data types is provided below
    to facilitate use of isinstance().
    
    Python datatypes: int, long, float, str, tuple, list, dict, xrange, slice
    
    Note: the assert statement can be silenced at compile time.  Python 
    documentation states, "If Python is started with the -O option, then 
    assertions will be stripped out and not evaluated." 
    
         (https://wiki.python.org/moin/UsingAssertionsEffectively) 
    """
  
    assert isinstance (a_float, float), 'This parameter is not a float!'
    assert isinstance (a_string, str), 'This parameter is not a string!'
        
    assert len (a_list) > 0, 'Parameter a_list is empty!'
    assert len (a_dict) > 0, 'Parameter a_dict is empty!'
    
    if not isinstance (a_float, float):
        print ('Parameter a_float is not a float!')
        return
        
    if not isinstance (a_string, str):
        print ('Parameter a_string is not a string!')
        return

    if not a_int in range (50, 100):
        print ('Parameter a_int must be between 50 and 100!')
        return

# Driver to test parameter_test ()

param_test (1234.45, 1234, 'Mayberry','Barney, Andy', sheriff='Andy')
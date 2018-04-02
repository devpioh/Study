while( True ):
    data = input( 'input data (quit : q): ' )
    if( 'q' == data ):
        print('bye bye')
        break;
    print( 'data : %s, type : %s'%(str(data), type(data)) )

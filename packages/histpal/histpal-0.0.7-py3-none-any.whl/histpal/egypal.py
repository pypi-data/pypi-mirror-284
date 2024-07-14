
#Ancient Egyptian Palettes


def egypal(type = 'Dendur' , n = 10):
    if (type == 'Dendur'):
        pal = ['#54786A', '#DED18D', '#AA5725','#EFCF83', '#624B1C']
        
       
    elif (type == 'tut'):
        pal = ['#964600', '#56645f', '#b74e16','#d5ac4a', '#47586f']
        
        
    elif (type == 'beetle'):
        pal = ['#40e0d0', '#1034a6', '#b70e00','#d4982d', '#7d4122']
        
            
    elif (type == 'ankh'):
        pal = ['#58c4e3', '#cb5500', '#c28f48','#41414a', '#b53406']    
        
            
    elif (type == 'anibus'):
        pal = ['#edd396', '#bd9f65', '#6d7781','#2c3b42', '#9d4530']
        
        
        
    return(pal[:n])

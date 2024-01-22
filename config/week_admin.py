

async def week_update(day, month):
    
    if month == 1:
        if day // 7 == 0:
            return day // 7
        else:
            return (day // 7) + 1
        
    elif month == 2:
        if (31+day) // 7 == 0:
            return (31+day) // 7
        else:
            return ((31+day) // 7) + 1
        
    elif month == 3:
        if (31+29+day) // 7 == 0:
            return (31+29+day) // 7
        else:
            return ((31+29+day) // 7) + 1
        
    elif month == 4:
        if (31+29+31+day) // 7 == 0:
            return (31+29+31+day) // 7
        else:
            return ((31+29+31+day) // 7) + 1
        
    elif month == 5:
        if (31+29+31+30+day) // 7 == 0:
            return (31+29+31+30+day) // 7
        else:
            return ((31+29+31+30+day) // 7) + 1
        
    elif month == 6:
        if (31+29+31+30+31+day) // 7 == 0:
            return (31+29+31+30+31+day) // 7
        else:
            return ((31+29+31+30+31+day) // 7) + 1
        
    elif month == 7:
        if (31+29+31+30+31+30+day) // 7 == 0:
            return (31+29+31+30+31+30+day) // 7
        else:
            return ((31+29+31+30+31+30+day) // 7) + 1
        
    elif month == 8:
        if (31+29+31+30+31+30+31+day) // 7 == 0:
            return (31+29+31+30+31+30+31+day) // 7
        else:
            return ((31+29+31+30+31+30+31+day) // 7) + 1
        
    if month == 9:
        if (31+29+31+30+31+30+31+31+day) // 7 == 0:
            return (31+29+31+30+31+30+31+31+day) // 7
        else:
            return ((31+29+31+30+31+30+31+31+day) // 7) + 1
        
    elif month == 10:
        if (31+29+31+30+31+30+31+31+30+day) // 7 == 0:
            return (31+29+31+30+31+30+31+31+30+day) // 7
        else:
            return ((31+29+31+30+31+30+31+31+30+day) // 7) + 1
        
    elif month == 11:
        if (31+29+31+30+31+30+31+31+30+31+day) // 7 == 0:
            return (31+29+31+30+31+30+31+31+30+31+day) // 7
        else:
            return ((31+29+31+30+31+30+31+31+30+31+day) // 7) + 1
        
    elif month == 12:
        if (31+29+31+30+31+30+31+31+30+31+30+day) // 7 == 0:
            return (31+29+31+30+31+30+31+31+30+31+30+day) // 7
        else:
            return ((31+29+31+30+31+30+31+31+30+31+30+day) // 7) + 1
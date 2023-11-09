def scoreaboard_print(rows): 
    for row in rows:
        print('|', ' | '.join(map(str,row)),'|') 
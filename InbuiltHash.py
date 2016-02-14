
"""Modifications for using inbuilt hash table (dictionary) in python.Redefine add_to_index and lookup procedures.Taking care not to add duplicate
entries of url to keyword"""
		
def add_to_index(index,keyword,url):                
#hash table implementation:adding keyword-url pair
    if keyword in index:
        index[keyword].append(url) 
    else:
	    index[keyword] = [url]
		

	
def lookup(index, keyword):                     
#hash table  searching for given word
    if keyword in index: 
	    return index[keyword] 
	else:
	    return None 

	
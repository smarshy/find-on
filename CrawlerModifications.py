
# Attempt to limit the pages that it can crawl.
# Procedure terminates the crawl after max_pages different pages have been crawled, or when there are no more pages to crawl.

def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl and len(crawled)<max_pages:
        
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

# Modified the crawl_web procedure to take a second parameter,max_depth, that limits the depth of the search. 
	
def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth=[]
    depth=0
    while tocrawl and depth<=max_depth:
        page = tocrawl.pop()
        
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl,next_depth=next_depth,tocrawl
            depth+=1
            
    return crawled

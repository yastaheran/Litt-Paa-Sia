#!/bin/bash

add="-a"
remove="-r"
bookmark_file=~/.my_bookmarks

# -a: add a bookmark pointing to the current directory
if [ "$1" == "$add" ]; then
	BNAME="$2"   
    # add the new bookmark to the file
	echo "$BNAME|`pwd`" >> "$bookmark_file"; 
	# source the file
    source "$bookmark_file" 

# -r: remove the bookmark with name
elif [ "$1" == "$remove" ]; then
	sed -e "s/$2|.*\$//" -e '/^$/ d' -i '' "$bookmark_file"
    unset $2

#read bookmark file
elif [ "$bookmark_file" = "$1" ]; then
	while IFS='|' read name dest; do
    	export $name=$dest
	done < "$1"
fi
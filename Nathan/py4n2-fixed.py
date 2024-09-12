#!/usr/bin/python3
dnaseq = "TATAGCCATGACCATATAGGATGTATA"
dna_array = list( dnaseq )
for nuc in dna_array: 
    print ( " ", nuc )
print ( "Done" )

size = len( dna_array )
search1 = "ATG"
search2 = "TATA"
search1found = 0
search2found = 0

# added a '-2' to the range because we are always looking 2 out
for i in range( size - 2 ):
    subseq = [ dna_array[i] , dna_array[i+1] , dna_array[i+2] ]
    subseq1 = ''.join( subseq )
    if ( subseq1 == search1):
        search1found = search1found + 1
# added an if and '-3' to size for our larger search term
    if ( i < size - 3 ):
        subseq.append( dna_array[i+3] )
        subseq2 = ''.join( subseq )
        if ( subseq2 == search2):
            search2found = search2found + 1

print ( search1found, " occurences of ", search1, " found in ", dnaseq )
print ( search2found, " occurences of ",  search2, " found in ", dnaseq )

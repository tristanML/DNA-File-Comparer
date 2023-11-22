# DNA-File-Comparer
Simple algorithm to compare two DNA strands. Takes input of two filenames(or two strings) and prints a list of segments found in both as well as the indices these segments are found.
  
__Examples:__  

Compares two files to find segments with 100 or more identical characters in a row 
```python
dna_comparison("sample1.txt","sample2.txt", False, 100)
```


Compares two string to find segments with 3 or more identical characters in a row
```python
dna_comparison("ACCATCGTAGA","CCTCGTAACCGTA", True, 3)
```

Prints:

>---Shared Segment #1---
>
>FILE 1 INDEX: 0-2
>
>FILE 2 INDEX: 7-9
>
>ACC
>
>---Shared Segment #2---
>
>FILE 1 INDEX: 4-8
>
>FILE 2 INDEX: 2-6
>
>TCGTA

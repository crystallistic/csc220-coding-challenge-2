'''

Authors: Mai Ngo, Sherri Lin
Assignment due date: February 15, 2018
Coding Challenge 2: Gene Splicing

Objective: given two strings representing snippets of genes (letters ACGT), identify the shortest string that could contain them both as subsequences.

Example:

********************************************
string 1 – AACCTGT     string 2 – CTGTACG
shortest string that has both as substring
AACCTGTACG (length 10)
********************************************

Description: This program consists of 3 funtions: gene_splicing_worker,
gene_splicing, and main. main will take in two strings from the user and call
gene_splicing. gene_splicing will call gene_splicing_worker, which is a worker
function that is only called inside gene_splicing that finds the shortest superstring
that contains both the strings supplied. gene_splicing finally compiles the
shortest superstring(s) that satisfy the condition and return them.

'''

def gene_splicing_worker(str1, str2):
  '''Worker function to find the shortest string that contains both of the given strings
  of gene snippets. Function works on the premise that
  we can find a length-l suffix of string X that matches a length-l prefix of
  string Y, and then extend this l until we find the longest match. Finally, we
  can form a new superstring using this overlap and the non-overlapping remaining
  parts of X and Y. 
  Parameters: 
  str1 - the first string
  str2 - the second string

  Return:
  super_str - a list of all the shortest superstrings that contain str1 and str2
  '''

  super_str = [] # list of shortest superstrings that match requirement
  match = '' # a superstring that matches the requirements so far

  # the lengths of the strings
  len1 = len(str1)
  len2 = len(str2)

  ''' find a length-i suffix of X that matches a length-i prefix of string Y
  and add new superstring to super_str. If shorter superstring found, empty
  super_str and append superstring.'''

  for l in range(1, len1-1):
    if str1[(len1-1-l):len1] == str2[0:(l+1)]:

      match = str1[0:(len1)-l-1] + str2

      # check first to see if this match is shorter than the one(s) already found
      if len(super_str) != 0 and len(match) < len(super_str[0]):
        super_str = [match]
      elif (len(super_str) == 0) or (len(super_str) != 0
                                     and len(match) == len(super_str[0])):
        super_str.append(match)

  # if the strings don't overlap anywhere, concatenate them
  if len(super_str) == 0:
    super_str.append(str1 + str2)
    
  return super_str
                                     
def gene_splicing(str1, str2):
  '''This function calls its worker function on two different ways of
  ordering the given strings and find the shortest superstring that contains
  the two given strings. This function works on the premise that the end of str1
  could match the beginning of str2 and the beginning of str1 could match the
  end of str2.

  Parameters:
  str1 - first small string
  str2 - second small string

  Return:
  super_str - a list of all the shortest superstrings that contain str1 and str2
  '''

  # call the gene splicing worker function
  super_str1 = gene_splicing_worker(str1,str2)
  super_str2 = gene_splicing_worker(str2,str1)
  
  super_str = [] # list of shortest superstrings after reviewing botch cases

  ''' Knowing that super_str1 and super_str2 contain the shortest possible
  superstring for each str1 and str2 arrangement, look for shortest possible
  superstring overall'''
  if len(super_str1) == 0:
    super_str = super_str2
  elif len(super_str2) == 0:
    super_str = super_str1
  else:
    shortest_len1 = len(super_str1[0])
    shortest_len2 = len(super_str2[0])
    if shortest_len1 > shortest_len2:
      super_str = super_str2
    elif shortest_len2 > shortest_len1:
      super_str = super_str1
    else:
      super_str = super_str1 + super_str2


  return super_str
    
def main():
  ''' Function that asks the user for two strings represent snippets of genes,
  and then call the gene_splicing() function on these strings to get the shortest 
  string(s) that contains these two strings'''

  # try-catch block to make sure the user inputted strings

  try: 
    
    # take 2 string inputs from user
    have_empty_str = True
    while have_empty_str:
      str1 = input("Please input string 1: ").strip().upper()
      str2 = input("Please input string 2: ").strip().upper()

      if len(str1) == 0 or len(str2) == 0:
        print("Empty strings are not accepted. Please try again.\n")
      else:
        have_empty_str = False
        
    # check if strings contain characters not belonging in a gene snippet
    str_lst = [str1, str2]
    for s in str_lst:
      print(s)
      for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'G' or s[i] == 'T' or s[i] == 'C':
          pass
        else:
          print("Strings are not case-sensitive and can only contain the characters [a,g,c,t]. Please try again.\n")
          main()
        
  
  except OSError: 
    
    print("Invalid input format, must be strings. Please try again.")
    main()

  super_str = gene_splicing(str1, str2)
        
  # output the shortest string containing the two inputted string
  print("\n********************************************************")
  print("string 1 -", str1, "\t", "string 2 -", str2)
  print("Shortest string(s) that has both as substring:")
  for s in super_str:
    print(s + " (length " + str(len(s)) + ")")
  print("********************************************************")
  


main()


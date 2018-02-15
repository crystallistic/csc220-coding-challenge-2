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

'''

def gene_splicing(str1, str2):
  '''Function to find the shortest string that contains both of the given strings of gene snippets
  Parameters: 
  str1 - the first string
  str2 - the second string'''
  stringslist = []
  result = []
 
  for c in str2:
    if c in str1:
      stringslist.append(c)
   
  if len(stringslist) == 0:
    result.append(str1+str2)
    result.append(str2+str1)
       
  else:
    result.append(str1.replace(max(stringslist, key=len), str2))  

  return result

def main():
  ''' Function that asks the user for two strings represent snippets of genes,
  and then call the gene_splicing() function on these strings to get the shortest 
  string that contains these two strings'''

  # try-catch block to make sure the user inputted strings
  try: 
    
    # take 2 string inputs from user
    str1 = input("Please input string 1: ").strip().upper()
    str2 = input("Please input string 2: ").strip().upper()
   
    # check if strings contain characters not belonging in a gene snippet
    for str in [str1, str2]:
      for i in range(len(str)):

        if str[i] == 'A' or str[i] == 'G' or str[i] == 'T' or str[i] == 'C':
          pass
        else:
          print("Strings are not case-sensitive and can only contain the characters [a,g,c,t]. Please try again.")
          main()
    

  except OSError: 
    
    print("Invalid input format, must be strings. Please try again.")
    main()

       
  # output the shortest string containing the two inputted string
  print(gene_splicing(str1, str2))

    

        
main()


# Coding Challenge 2

def gene_splicing(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    stringslist = []
    result = []
    substrings = [str2[i:j+1] for i in range(len(str2)) for j in range(i, len(str2))]

    for string in substrings:
        if string in str1:
            stringslist.append(string)
    
    if len(stringslist) == 0:
        result.append(str1+str2)
        result.append(str2+str1)
        
    else:
        result.append(str1.replace(max(stringslist, key=len), str2))   

    return result


def main():
  '''Place holder here for description later'''
  try:
      string1 = input("String 1: ")
      string2 = input("String 2: ")
  except OSError:
      print("Invalid")

  print(gene_splicing(string1, string2))



main()



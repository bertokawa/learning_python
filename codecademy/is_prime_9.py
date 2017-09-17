def is_prime (x):
  num = x / 2 +1
  cont = 2
  prime = 0

  print ("x: " + str(x))
  
  while (cont <= num):
    print ("cont: " + str(cont))
    
    if (x % cont == 0):
      prime += 1

    print ("x % cont: " + str(x % cont))
    print ("prime: " + str(prime))
    cont += 1
    
  if (prime > 1):
    return False
    
  else:
    return True
  
print (is_prime(17))

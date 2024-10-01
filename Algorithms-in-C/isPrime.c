bool isPrime(int n) {
  if(n<2) return false;
  if(n%2==0) return (n==2);
  int root=sqrt(n);
  for(int i=3; i<root; i+=2)
    if(n%i==0)
      return false;
  return true;
}
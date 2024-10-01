int power(int x, int y, int mod) {
  int res=1;
  x=x%mod;
  while(y) {
    if(y&1) res=res*x%mod;
    x=x*x%mod;
    y>>=1;
  }
  return res;
}
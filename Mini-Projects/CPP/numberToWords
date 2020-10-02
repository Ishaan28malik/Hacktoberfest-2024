string numberToWords(int n) {
	array<string, 16> nums  = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
							  "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen"};
	array<string, 5> var = {"Twen", "Thir", "For", "Fif", "Eigh"};
	auto variant = [&nums, &var](int n) ->const string& {if(n < 6) return var[n-2]; return n==8?var[4]:nums[n];};
	const int H = 100, T = 1000, M = 1000 * T, B = 1000 * M;
	if(n < 16)
		return nums[n];
	else if(n < 20)
		return string(variant(n-10))+"teen";
	else if(n < H)
		return string(variant(n/10))+"ty" + (n%10?" " + nums[n%10]:"");
	else if(n < T)
		return nums[n/H] + " Hundred" + (n%H?" "+numberToWords(n%H):"");
	else if(n < M)
		return numberToWords(n/T) + " Thousand" + (n%T?" "+numberToWords(n%T):"");
	else if(n < B)
		return numberToWords(n/M) + " Million" + (n%M?" "+numberToWords(n%M):"");
	return numberToWords(n/B) + " Billion" + (n%B?" "+numberToWords(n%B):"");
}

int main(){
  int num;
  cout<<"Enter a number: ";
  cin>>num;
  string res = numberToWords(num);
  cout<<"\nResult : "<<res;
  return 0;
}

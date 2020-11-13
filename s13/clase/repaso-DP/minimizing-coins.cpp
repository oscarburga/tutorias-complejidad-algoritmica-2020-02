#include <bits/stdc++.h>
using namespace std;
 
const int maxn = 105, maxs = 1e6+5;
int n, x, a[maxn], dp[maxs];
 
int main(){
	scanf("%d %d", &n, &x);
	for(int i = 1; i<=n; i++) scanf("%d", &a[i]);
	fill(dp+1, dp+maxs, maxs);
	for(int i = 1; i<=n; i++){
		for(int s = a[i]; s<=x; s++) dp[s] = min(dp[s], dp[s-a[i]] + 1);
	}
	printf("%d\n", dp[x] == maxs ? -1 : dp[x]);
 
	return 0;
}

// Link al problema: https://codeforces.com/contest/1385/problem/D
// Solución en C++

#include <bits/stdc++.h>
using namespace std;

const int maxn = 2e5+5, inf = 1e6;

int n;
char s[maxn];

int solve(int l, int r, char f){
	if (l == r) return s[l] != f;
	if (f == 'z' && l != r) return inf;
	int mid = (l+r)/2;
	int costL = 0, costR = 0;
	for(int i = l; i <= mid; i++) costL += (s[i] != f);
	costL += solve(mid+1, r, f + char(1));
	for(int i = mid+1; i <= r; i++) costR += (s[i] != f);
	costR += solve(l, mid, f + char(1));
	return min(costL, costR);
}

int main(){
	int tc; scanf("%d", &tc);
	while(tc--){
		scanf("%d", &n);
		scanf("%s", s);
		int ans = solve(0, n-1, 'a');
		printf("%d\n", ans);
	}
	return 0;
}


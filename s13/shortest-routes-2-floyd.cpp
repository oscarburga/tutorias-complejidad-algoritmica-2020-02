#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int maxn = 505;
const ll inf = 1e18;
int n, m, q;
ll d[maxn][maxn];

int main(){
	scanf("%d %d %d", &n, &m, &q);
	for(int i = 0; i<n; i++) {
		fill(d[i], d[i]+n, inf);
		d[i][i] = 0;
	}
	for(int i = 0; i<m; i++) {
		int x, y, w;
		scanf("%d %d %d", &x, &y, &w);
		x--, y--;
		d[x][y] = d[y][x] = min(d[y][x], (ll)w);
	}
	for(int k = 0; k<n; k++) 
		for(int i = 0; i<n; i++) 
			for(int j = 0; j<n; j++) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	
	while(q--){
		int x, y;
		scanf("%d %d", &x, &y);
		x--, y--;
		printf("%lld\n", d[x][y] >= inf ? -1 : d[x][y]);
	}
	return 0;
}


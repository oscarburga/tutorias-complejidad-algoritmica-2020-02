// Shortest Routes II del CSES con Johnson
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int maxn = 505;
const ll inf = 1e18;
int n, m, q;
bool vis[maxn][maxn];
ll w[maxn][maxn], h[maxn], d[maxn][maxn];

void dijkstra(int src) { 
	d[src][src] = 0;
	for(int i = 0; i<n; i++) {
		ll curd = inf;
		int v = -1;
		for(int j = 0; j<n; j++) {
			if (!vis[src][j] && d[src][j] < curd) {
				v = j;
				curd = d[src][j];
			}
		}
		if (v == -1) break;
		vis[src][v] = true;
		for(int j = 0; j<n; j++) {
			d[src][j] = min(d[src][j], d[src][v] + w[v][j]);
		}
	}
}

void bellman() { 
	fill(h, h+n, 0);
	for(int k = 0; k<n-1; k++) {
		for(int u = 0; u<n; u++) {
			for(int v = 0; v<n; v++) {
				h[v] = min(h[v], h[u] + w[u][v]);
			}
		}
	}
}

void johnson() {
	bellman();
	for(int i = 0; i<n; i++) {
		for(int j = 0; j<n; j++) {
			if (w[i][j] < inf) w[i][j] += h[i] - h[j];
		}
	}
	for(int i = 0; i<n; i++) {
		dijkstra(i);
		for(int j = 0; j<n; j++) d[i][j] += h[j] - h[i];
	}
}

int main(){
	scanf("%d %d %d", &n, &m, &q);
	for(int i = 0; i<n; i++) {
		fill(w[i], w[i]+n, inf);
		fill(d[i], d[i]+n, inf);
	}
	for(int i = 0; i<m; i++) {
		int x, y, c;
		scanf("%d %d %d", &x, &y, &c);
		x--, y--;
		w[x][y] = w[y][x] = min(w[y][x], (ll)c);
	}
	johnson();
	while(q--){
		int x, y;
		scanf("%d %d", &x, &y);
		x--, y--;
		printf("%lld\n", d[x][y] >= inf ? -1 : d[x][y]);
	}
	return 0;
}


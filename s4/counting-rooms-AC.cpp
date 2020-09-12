// Solución del Counting Rooms en C++ (si pasa el tiempo límite)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
 
const int maxn = 1e3+5;
const int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
int n, m;
bool vis[maxn][maxn];
char mat[maxn][maxn];
 
bool valid(int r, int c, int i){
	r += dx[i], c += dy[i];
	return (r >=1 && r<=n && c >= 1 && c<=m && !vis[r][c] && mat[r][c] == '.');
}
 
void dfs(int r, int c){
	vis[r][c] = true;
	for(int i = 0; i<4; i++) if (valid(r, c, i)) dfs(r+dx[i], c+dy[i]);
}
 
int main(){
	scanf("%d %d", &n, &m);
	for(int i = 1; i<=n; i++){
		scanf("%s", mat[i]+1);
	}
	int ans = 0;
	for(int i = 1; i<=n; i++){
		for(int j = 1; j<=m; j++) 
			if (mat[i][j] == '.' && !vis[i][j]) 
				ans++, dfs(i, j); 
	}
	printf("%d\n", ans);
 
	return 0;
}

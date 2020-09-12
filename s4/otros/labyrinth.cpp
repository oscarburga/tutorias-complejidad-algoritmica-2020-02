// Este problema queda pendiente para el siguiente taller
// https://cses.fi/problemset/task/1193/
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int maxn = 1e3+5;
const int dx[4] = { 1, -1, 0, 0 }, dy[4] = { 0, 0, 1, -1 };
string dd = "DURL";
int n, m, p[maxn][maxn];
char mat[maxn][maxn];

bool valid(int r, int c, int i){
	r += dx[i], c += dy[i];
	return r>=0 && r<n && c>=0 && c < m && p[r][c] == -1 && mat[r][c] != '#';
}

int main(){
	scanf("%d %d\n", &n, &m);
	pair<int,int> start, end;
	for(int i = 0; i<n; i++){
		for(int j = 0; j<m; j++){
			mat[i][j] = getchar();
			if (mat[i][j] == 'A') start = {i, j};
			if (mat[i][j] == 'B') end = {i, j};
		}
		getchar();
	}
	memset(p, -1, sizeof(p));
	queue<pair<int,int>> q;
	p[start.first][start.second] = -2;
	q.push(start);
	while(q.size()){
		if (q.front() == end) break;
		int r = q.front().first, c = q.front().second;
		q.pop();
		for(int i = 0; i<4; i++) if (valid(r, c, i)) {
			int nr = r+dx[i], nc = c+dy[i];
			p[nr][nc] = i;
			q.push({nr, nc});
		}
	}
	if (p[end.first][end.second] == -1) { puts("NO"); return 0; }
	int r = end.first, c = end.second;
	vector<char> ans;
	while(p[r][c] >= 0) {
		int i = p[r][c];
		ans.emplace_back(dd[i]);
		r -= dx[i], c -= dy[i];
	}
	reverse(ans.begin(), ans.end());
	puts("YES");
	printf("%zu\n", ans.size());
	for(char x: ans) putchar(x);
	puts("");
	return 0;
}


#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int maxn = 5e3+5, maxv = 1e4+5;
vector<int> s[maxv], e[maxv];
int h[maxv];

int main(){
	int l, r, x;
	while(scanf("%d %d %d", &l, &x, &r) != EOF){
		s[l].emplace_back(x);
		e[r].emplace_back(x);
	}
	multiset<int> hs;
	vector<int> ans;
	hs.emplace(0);
	int curh = 0;
	for(int i = 0; i<maxv; i++){
		for(int x: s[i]) hs.emplace(x);
		for(int x: e[i]) hs.erase(hs.find(x));
		h[i] = *hs.rbegin();
		if (h[i] != curh) {
			ans.emplace_back(i);
			ans.emplace_back(h[i]);
			curh = h[i];
		}
	}
	for(int i = 0; i<ans.size(); i++) printf("%d%c", ans[i], " \n"[i+1==ans.size()]);
	return 0;
}

/*
Solución al problema Skylines sin usar Divide y Vencerás.
Complejidad: O(MAX + NlogN), donde MAX = máximo valor que pueden darte como coordenada X. 
Fácilmente optimizable a O(NlogN) evaluando sólo los puntos donde inician y acaban edificios.

Para este caso, MAX = 10000, N = 5000.
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=41
*/

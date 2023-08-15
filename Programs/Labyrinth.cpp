
#include <bits/stdc++.h>
using namespace std;


bool isValid(vector<vector<bool>>& vis,int x,int y,int &n,int &m){
  if(x<0||y<0||x>=n||y>=m){
    return false;
  }
  if(vis[x][y]==1){
    return false;
  }
  return true;
}
bool bfs(vector<vector<bool>> &vis, int &i, int &j, int &u, int &v; int &n, int &m)
{
  queue<pair<int,int>> q;
  q.push({i, j});
  vector<pair<int, int>> moves={{-1,0},{1,0},{0,1},{0,-1}};
  while(!q.empty()){
  vis[i][j] = 1;
  pair<int, int> p = q.front();
  q.pop();
  for (int k = 0; k < 4;k++){
    int x = p.first + moves[k].first;
    int y = p.second + moves[k].second;
    if(isValid(vis,x,y,n,m)){
      if(x==u&&y==v){
        return true;
      }
      q.push({x, y});
    }
  } 
  }
string bfs(vector<vector<bool>> &vis, int &i, int &j, int &u, int &v; int &n, int &m)
{
  queue<pair<int,int>> q;
  q.push({i, j});
  vector<pair<pair<int, int>,char >> moves={{-1,0,U},{1,0,D},{0,1,R},{0,-1,L}};
  while(!q.empty()){
  vis[i][j] = 1;
  pair<int, int> p;
  p = q.front();
  q.pop();
  
  
  
}
int main()
{
  
  int n, m;
  cin >> n >> m;
  char a[n][m];
  vector<vector<bool>> vis(n, vector<bool> (m));
  string x;
  int p, q, r, s;
  for (int i = 0; i <n;i++){
    {
      /* code */
      cin >> a[i][j];
      if(a[i][j]=='A'){
        p = i;
        q = j;
      }
      if(a[i][j]=='A'){
        r = i;
        s = j;
      }

    }
  }
  for (int i = 0; i < n;i++){
    for (int j = 0; j < m;j++){
      if(a[i][j]=='#'){
        vis[i][j] = 1;
        continue;}
      
      vis[i][j] = 0;
      
    } 
  }
  bool ans = false;
  ans=dfs(vis, p, q,r,s n, m);
  if(ans){
    cout << "YES" << endl;
  }
  else{
    cout << "NO" << endl;
  }
   
}
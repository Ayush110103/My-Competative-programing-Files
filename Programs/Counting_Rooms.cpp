
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
void dfs(vector<vector<bool>>& vis,int &i,int &j,int &n,int &m){
  vector<pair<int, int>> moves={{-1,0},{1,0},{0,1},{0,-1}};
  vis[i][j] = 1;
  for (auto move : moves)
  {
    int x = i + move.first;
    int y = j + move.second;
    if(isValid(vis,x,y,n,m)){
      dfs(vis, x, y,n,m);
    }
  }
}
int main()
{
  
  int n, m;
  cin >> n >> m;
  char a[n][m];
  vector<vector<bool>> vis(n, vector<bool> (m));
  string x;
  for (int i = 0; i <n;i++){
    for (int j = 0; j < m; j++)
    {
      /* code */
      cin >> a[i][j];
    }
  }
  for (int i = 0; i < n;i++){
    for (int j = 0; j < m;j++){
      if(a[i][j]=='#'){
        vis[i][j] = 1;
      }
      else{
        vis[i][j] = 0;
      }
    } 
  }
  int count = 0;
   for (int i = 0; i < n;i++){
    for (int j = 0; j < m;j++){
  if(!vis[i][j]){
        dfs(vis, i, j,n,m);
        ++count;
  }
}
   }
    cout << count;
}
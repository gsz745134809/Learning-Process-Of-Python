//ECUST luoyongjun
#include<bits/stdc++.h>
const int INF = 1e9;
const int maxn = 300;
using namespace std;
int n, m, map_[maxn][maxn], pre[maxn];
    // map_[][]������¼ͼ�����ǲ�������
int bfs(int s,int t){
    int flow[maxn];
    memset(pre,-1,sizeof pre);
    flow[s]=INF; pre[s] = 0;            //��ʼ�����
    queue<int> Q;  Q.push(s);           //�����ջ����ʼbfs
    while(!Q.empty()){
        int u = Q.front();  Q.pop();
        if(u==t) break;                  //�ѵ�һ��·�������bfs����
        for(int i=1; i<=m; i++){        //bfs���еĵ�
            if(i!=s && map_[u][i]>0 && pre[i]==-1){
                pre[i] = u;  		    //��¼·��
                Q.push(i);
                flow[i] = min(flow[u], map_[u][i]); //���½������
            }
        }
    }
    if(pre[t]==-1) return -1;           //û���ҵ��µ�����·
    return flow[t];                       //�����������·������
}
int maxflow(int s, int t){
    int Maxflow = 0;
    while(1){
        int flow = bfs(s,t);
//ִ��һ��bfs���ҵ�һ��·��������·��������
        if(flow == -1) break;             //û���ҵ��µ�����·������
        int cur = t;                        //����·���ϵĲ�������
        while(cur!=s){                      //һֱ��·�����ݵ����
            int father = pre[cur];        //pre[]��¼·���ϵ�ǰһ����
            map_[father][cur] -= flow;    //���²������磺�����
            map_[cur][father] += flow;    //���²������磺�����
            cur = father;
        }
        Maxflow += flow;
    }
    return Maxflow;
}
int main(){
    while(~scanf("%d%d",&n,&m)){
        memset(map_,0,sizeof map_);
        for(int i=0; i<n; i++){
            int u,v,w;
            scanf("%d%d%d",&u,&v,&w);
            map_[u][v]+=w;            //�������ر�
        }
        printf("%d\n",maxflow(1,m));
    }
    return 0;
}

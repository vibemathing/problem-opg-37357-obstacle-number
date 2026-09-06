// Candidate bounded CDCL producer. Each learned clause is logged as a RUP addition.
// No claim of verifier admission. Compile with C++17. Input DIMACS, output text RUP.
#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
struct Solver {
 int n,head=0; vector<vector<int>> cls,watch; vector<int> val,lev,why,trail,lim,phase; vector<double> act; vector<char> seen;
 double inc=1; long conflicts=0,decisions=0,proofbytes=0; ofstream proof; chrono::steady_clock::time_point started;
 int idx(int l){return 2*(abs(l)-1)+(l<0);} int dl(){return (int)lim.size();}
 int value(int l){return val[abs(l)]*(l>0?1:-1);}
 Solver(int nn,const string& p):n(nn),watch(2*nn),val(nn+1),lev(nn+1),why(nn+1,-1),phase(nn+1,1),act(nn+1),seen(nn+1),proof(p),started(chrono::steady_clock::now()){}
 bool enqueue(int l,int r){int v=abs(l),s=l>0?1:-1;if(val[v])return val[v]==s;val[v]=s;phase[v]=s;lev[v]=dl();why[v]=r;trail.push_back(l);return true;}
 int add(vector<int> c){int id=cls.size();cls.push_back(move(c)); if(cls[id].size()>1){watch[idx(cls[id][0])].push_back(id);watch[idx(cls[id][1])].push_back(id);} return id;}
 int propagate(){
  while(head<(int)trail.size()){
   int f=-trail[head++]; auto &ws=watch[idx(f)]; size_t j=0;
   while(j<ws.size()){
    int id=ws[j];auto &c=cls[id]; if(c[0]!=f)swap(c[0],c[1]);
    if(c[0]!=f){cerr<<"watch invariant\n";exit(5);} int other=c[1];
    if(value(other)==1){j++;continue;}
    int k=2;while(k<(int)c.size()&&value(c[k])==-1)k++;
    if(k<(int)c.size()) {swap(c[0],c[k]);watch[idx(c[0])].push_back(id);ws[j]=ws.back();ws.pop_back();continue;}
    if(value(other)==-1)return id;
    if(!enqueue(other,id))return id;
    j++;
   }
  }return -1;
 }
 void cancel(int level){if(dl()<=level)return;int cutoff=lim[level];for(int i=(int)trail.size()-1;i>=cutoff;i--){val[abs(trail[i])]=0;why[abs(trail[i])]=-1;}trail.resize(cutoff);head=min(head,cutoff);lim.resize(level);}
 void bump(int v){act[v]+=inc;if(act[v]>1e100){for(double &a:act)a*=1e-100;inc*=1e-100;}}
 pair<vector<int>,int> analyze(int confl){
  vector<int> out(1,0), touched;int count=0,p=0,pos=(int)trail.size()-1,cid=confl;
  do {
   if(cid<0){cerr<<"missing reason\n";exit(5);}
   for(int q:cls[cid]){int v=abs(q);if(v==abs(p)||seen[v]||lev[v]==0)continue;seen[v]=1;touched.push_back(v);bump(v);if(lev[v]==dl())count++;else out.push_back(q);}
   while(pos>=0&&!seen[abs(trail[pos])])pos--;
   if(pos<0){cerr<<"analysis invariant\n";exit(5);}
   p=trail[pos--];seen[abs(p)]=0;count--;cid=why[abs(p)];
  }while(count>0);
  out[0]=-p;int back=0,best=1;for(int i=1;i<(int)out.size();i++)if(lev[abs(out[i])]>back){back=lev[abs(out[i])];best=i;}
  if(out.size()>1)swap(out[1],out[best]);for(int v:touched)seen[v]=0;
  inc/=0.95;return {out,back};
 }
 void log(const vector<int>&c){for(int l:c){proof<<l<<' ';proofbytes+=to_string(l).size()+1;}proof<<"0\n";proofbytes+=2;}
 int solve(){long restart=100,next=100;while(true){
   if(conflicts%256==0){double elapsed=chrono::duration<double>(chrono::steady_clock::now()-started).count();if(elapsed>55||proofbytes>6000000||conflicts>200000)return 0;}
   int confl=propagate();
   if(confl>=0){conflicts++;if(dl()==0){log({});return -1;}auto [learn,back]=analyze(confl);log(learn);cancel(back);int id=add(learn);if(!enqueue(learn[0],id)){cerr<<"asserting invariant\n";return 2;}if(conflicts>=next){cancel(0);restart=min((long)(restart*1.5),10000L);next=conflicts+restart;}continue;}
   int v=0;double score=-1;for(int i=1;i<=n;i++)if(!val[i]&&act[i]>score){score=act[i];v=i;}if(!v)return 1;
   decisions++;lim.push_back(trail.size());enqueue(v*phase[v],-1);
  }}
};
int main(int argc,char**argv){
 if(argc!=3){cerr<<"usage: producer CNF RUP\n";return 2;}ifstream in(argv[1]);string s;int n=0,m=0;
 while(getline(in,s)){if(s.empty()||s[0]=='c')continue;if(s[0]=='p'){istringstream st(s);string p,t;st>>p>>t>>n>>m;break;}}
 if(n<1||n>5000||m<1||m>200000){cerr<<"invalid or refused dimensions\n";return 3;}Solver sol(n,argv[2]);vector<int> c;int l;bool contradiction=false;
 while(in>>l){if(l){if(abs(l)>n)return 2;c.push_back(l);}else{int id=sol.add(c);for(int z:c)sol.act[abs(z)]+=1.0/(1+c.size());if(c.empty())contradiction=true;else if(c.size()==1&&!sol.enqueue(c[0],id))contradiction=true;c.clear();}}
 if(!c.empty()||(int)sol.cls.size()!=m)return 2;
 int result;if(contradiction){sol.log({});result=-1;}else result=sol.solve();
 sol.proof.flush();double elapsed=chrono::duration<double>(chrono::steady_clock::now()-sol.started).count();
 cout<<"{\"status\":\""<<(result==-1?"UNSAT":result==1?"SAT":result==0?"UNKNOWN_BUDGET":"INTERNAL_ERROR")<<"\",\"conflicts\":"<<sol.conflicts<<",\"decisions\":"<<sol.decisions<<",\"rup_bytes\":"<<sol.proofbytes<<",\"seconds\":"<<elapsed<<"}\n";
 if(result==1){cout<<"v ";for(int i=1;i<=n;i++)cout<<i*sol.val[i]<<' ';cout<<"0\n";}return result==-1?20:result==1?10:result==0?0:5;
}

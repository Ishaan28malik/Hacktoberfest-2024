
//If it has Directed edges

import java.util.*;
class GraphCycle{
	int v;
	LinkedList<Integer> adj[];
	GraphCycle(int v){
		this.v=v;
		adj=new LinkedList[v];
		for(int i=0;i<v;i++)
			adj[i]=new LinkedList<>();
	}
	private boolean isCyclicUtil(int i,boolean[] visited,boolean[] recstack)
	{
		if(recstack[i])
			return true;
		if(visited[i])
			return false;
		visited[i]=true;
		recstack[i]=true;
		List<Integer> child=adj[i];
		for(Integer c:child)
			if(isCyclicUtil(c,visited,recstack))
				return true;
		recstack[i]=false;
		return false;
	}
	private boolean isCyclic()
	{
		boolean[] visited=new boolean[v];
		boolean[] recstack=new boolean[v];
		
		for(int i=0;i<v;i++)
			if(isCyclicUtil(i,visited,recstack))
				return true;
		return false;
	}
	private void addEdge(int Start,int End){
		adj[Start].add(End);
	}
	public static void main(String[] args) 
	{ 
		GraphCycle graph = new GraphCycle(4); 
		graph.addEdge(0, 1); 
		graph.addEdge(0, 2); 
		graph.addEdge(1, 2); 
		graph.addEdge(2, 0); 
		graph.addEdge(2, 3); 
		graph.addEdge(3, 3); 
		
		if(graph.isCyclic()) 
			System.out.println("Graph contains cycle"); 
		else
			System.out.println("Graph doesn't "
									+ "contain cycle"); 
	} 
}
/*
//If it has non Directed edges
class DetectCycle
{
    static boolean isCyclicUtil(ArrayList<ArrayList<Integer>> list,int v,boolean[] visited,int parent)
	{
	    visited[v]=true;
		List<Integer> child=list.get(v);
		for(Integer i:child)
		{
		    if(!visited[i])
		    {
			    if(isCyclicUtil(list,i,visited,v))
				    return true;
		    }
		    else if(i!=parent)
		        return true;
		}
		return false;
	}
    static boolean isCyclic(ArrayList<ArrayList<Integer>> list, int v)
    {
        // add your code here
        boolean[] visited=new boolean[v];
		for(int i=0;i<v;i++)
		    if(!visited[i])
		        if(isCyclicUtil(list,i,visited,-1))
				    return true;
		return false;
        
    }
}

*/
 
	
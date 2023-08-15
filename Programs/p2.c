#include <stdio.h>
#include <stdlib.h>

#define MAX_N 100000

typedef struct {
    int** a;
    int* visited;
    int* count;
    int n;
} Graph;

void dfs(int i, Graph* graph, int start, int* cycle, int length) {
    int** a = graph->a;
    int* visited = graph->visited;
    
    if (!visited[i]) {
        visited[i] = 1;
        dfs(a[i][0], graph, start, cycle, length + 1);
        if (a[i][1] != 0)
            dfs(a[i][1], graph, start, cycle, length + 1);
    } else {
        if (i == start) {
            if (length != 2) {
                (*cycle)++;
            }
        }
        return;
    }
}

Graph* createGraph(int n) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    
    graph->n = n;
    graph->a = (int**)malloc((n + 1) * sizeof(int*));
    graph->visited = (int*)calloc(n + 1, sizeof(int));
    graph->count = (int*)calloc(n + 1, sizeof(int));
    
    for (int i = 0; i <= n; i++) {
        graph->a[i] = (int*)calloc(2, sizeof(int));
    }
    
    return graph;
}

void freeGraph(Graph* graph) {
    int n = graph->n;
    
    for (int i = 0; i <= n; i++) {
        free(graph->a[i]);
    }
    
    free(graph->a);
    free(graph->visited);
    free(graph->count);
    free(graph);
}

void processGraph(Graph* graph) {
    int n = graph->n;
    int** a = graph->a;
    int* visited = graph->visited;
    int* count = graph->count;
    
    int cycles = 0;
    int comp = 0;

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            comp++;
            dfs(i, graph, i, &cycles, 0);
        }
    }

    int x = 1;
    if (cycles == comp) {
        x = 0;
    }

    printf("%d %d\n", cycles + x, comp);
}

int main() {
    int t = 1;
    // scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        Graph* graph = createGraph(n);

        for (int i = 1; i <= n; i++) {
            scanf("%d", &graph->a[i][0]);
        }

        for (int i = 1; i <= n; i++) {
            if (graph->a[graph->a[i][0]][0] != i) {
                graph->a[graph->a[i][0]][1] = i;
            }
        }

        processGraph(graph);

        freeGraph(graph);
    }

    return 0;
}

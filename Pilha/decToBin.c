#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct pilha Pilha;

struct elemento{
	int info;

	struct elemento * prox;
};

typedef struct elemento Elemento;

struct pilha{
	
	Elemento * topo;
};

/*criando a pilha*/
Pilha * pilha_cria(void){
	
	Pilha * p = (Pilha *) malloc(sizeof(Pilha));
	
	p->topo = NULL;
	
	return p;
}

/*verificar se a pilha está vazia*/
int pilha_vazia(Pilha * p){

	return (p->topo == NULL);
}


/*inserir elemento na pilha*/
void pilha_push(Pilha * p, int a){
	
	Elemento * novo = (Elemento *)malloc(sizeof(Elemento));
	
	assert(novo != NULL);
	
	novo->info = a;
	
	novo->prox = p->topo;
	
	p->topo = novo;
}


/*remover elemento na pilha*/
int pilha_pop(Pilha * p){
	
	Elemento * t;
	
	int a;
	
	assert(!pilha_vazia(p));
	
	t = p->topo;
	
	a = t->info;
	
	p->topo = t->prox;
	
	free(t);
	
	return a;
}

/*liberando espaço na pilha*/
void pilha_libera(Pilha * p){
	
	Elemento *t, * q = p->topo;
	
	while (q != NULL){
	
		t = q->prox;
	
		free(q);
	
		q = t;
	}
	
	free(p);
}


/*protótipo da função*/
void dec2bin(int n, char * t);

/*função que passa valor decimal para binário usando pilha*/
void dec2bin(int n, char * t){

	Pilha * p = pilha_cria();

	do{
		pilha_push(p,n%2);

		n /= 2;
	} while (n);

	while (!pilha_vazia(p))

	*t++ = '0'+ pilha_pop(p);
	
	*t = '\0';
	
	pilha_libera(p);
}

int main(void){

	char bin[10];

	int n;

	scanf("%d", &n);

	dec2bin(n,bin);

	printf("%d (decimal) -> %s (binário)\n",n,bin);
	
	return 0;
}

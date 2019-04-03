//###### LISTA ENCADEADA ######//
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct dataNode{

	int id;
	
}DataNode;

typedef struct node{
	
	DataNode data;

	struct node* next;

}Node;

typedef struct list{

	int size;

	Node* head;

}List;

////////HEADER->Protótipo de funções//////////////////

List* createList(); //cria a lista

void push(List* list, DataNode data); //inserir um nó na lista

void printList(List* list); //imprimi a lista

void pop(List* list); //exclui o primeiro nó da lista

bool isEmpty(List* list); //verifica se a lista está vazia

Node* atPos(List* list, int index); //Mostra o valor do nó com o índex solicitado (caso não exista, retorna NULL)

int indexOf(List* list, Node* node); //retorna o nó especificado na lista (caso não esteja, retorna -1)

void erase(List* list, int index); //exclui um nó especificado pelo index

void insert(List* list, DataNode data, int index); //inserir um nó especificando um index e posição

void xchgNodes(List* list, Node* nA, Node* nB); //troca dois nós de posição

Node* min(List *list, int index); //retorna um valor mínimo da lista a partir do índice especificado

Node* max(List *list, int index); //retorna um valor máximo da lista a partir do índice especificado

void cSort(List* list); //ordena a lista em ordem crescente

void dSort(List* list); //ordena a lista em ordem decrescente

//***************************************************//****************************************

void push(List* list, DataNode data){

	Node* node = (Node*) malloc(sizeof(Node));

	node->data = data;

	node->next = list->head;

	list->head = node;

	list->size++;
}



List* createList(){

	List* list = (List*) malloc(sizeof(List));

	list->size = 0;

	list->head = NULL;

	return list;

}



void printList(List* list){

	Node* pointer = list->head;

	if(isEmpty(list)){
		printf("Lista vazia.");
		return;
	}

	printf("Valores da lista: ");
	while(pointer != NULL){
		printf("%d ",pointer->data.id);

		pointer = pointer->next;
	}

	printf("\n");
}



bool isEmpty(List* list){
	
	return (list->size == 0);
}



void pop(List* list){

	if(!isEmpty(list)){
		
		Node* pointer = list->head; //ponteiro auxiliar para cabeça da lista
	
		list->head = pointer->next; //mudando a cabeça da lista para o próximo nó
	
		free(pointer); //libra espaço da memória excluindo o nó

		list->size --;
	}
}



Node* atPos(List *list, int index){

	if(index >= 0 && index < list->size){
		
		Node* node = list->head;

		for(int i = 0; i <index; i++)
			node = node->next;

		return node;
	}

	return NULL;
}



int indexOf(List* list, Node* node){

	if(node != NULL){
		Node* pointer = list->head;

		int index = 0;

		while(pointer != node && pointer != NULL){
			
			pointer = pointer->next;
			
			index+=1;
		}

		if(pointer != NULL)
			return index;
	}

	printf("Nó não pertence à lista.\n");
	
	return -1;
}



void erase(List* list, int index){

	if(index == 0)
		pop(list);

	else{
		
		Node* current  = atPos(list, index);

		if(current != NULL){
			
			Node* previous = atPos(list, index - 1); //ponteiro para posição anterior à excluída
			
			previous->next = current->next; //ponteiro aponta para variável próxima a qual foi excluída
			
			free(current); //libra espaço da memória excluindo o nó solicitado pelo index

			list->size--; //reduz o tamanho da lista
		}
	}
}

void insert(List *list, DataNode data, int index){
	if(index == 0) 
		push(list, data); //se o índice solicitado for 0, ele faz a função push

	else{
		
		Node* current = atPos(list, index); //um nó de apoio recebe o índice solicitado
	
		if(current != NULL){
			Node* previous = atPos(list, index-1); //outro nó recebe a posição anterior do índice solicitado

			Node* novo = (Node*) malloc(sizeof(Node)); //armazena o novo nó na memória dinamicamente

			novo->data = data; //nó recebe o conteúdo passado na função

			previous->next = novo; //índice sucessor recebe o valor do nó previous

			novo->next = current; //o novo nó é atribuído à posição do nó current

			list->size++; //aumenta o tamanho da lista, conforme a inserção de um novo nó
		}
	}
}



void xchgNodes(List* list, Node* nA, Node* nB){
	
	if(nA == nB){
		return;
	}

	int indexA = indexOf(list, nA);

	int indexB = indexOf(list, nB);

	if(indexA > indexB){
		nA = nB;
		
		nB = atPos(list, indexA);

		indexA = indexB;

		indexB = indexOf(list, nB);
	}

	Node* pb = atPos(list, indexB-1);

	if(nA == list->head)
		list->head = nB;

	else{
		Node* pa = atPos(list, indexA-1);
	
		pa->next = nB;
	}

	pb->next = nA;

	Node* pointer = nA->next;
	
	nA->next = nB->next;

	nB->next = pointer;
}


Node* min(List *list, int index){

	Node* pointer = atPos(list, index);

	if(pointer != NULL){
		Node* minNode = pointer;

		while(pointer != NULL){
			
			if(pointer->data.id < minNode->data.id)
				minNode = pointer;

			pointer = pointer->next;
		}

		return minNode;
	}

	return NULL;
}


Node* max(List *list, int index){

	Node* pointer = atPos(list, index);

	if(pointer != NULL){
		Node* maxNode = pointer;
	
		while(pointer != NULL){
			if(pointer->data.id > maxNode->data.id)
				maxNode = pointer;

			pointer = pointer->next;
		}

		return maxNode;
	}

	return NULL;
}


void cSort(List *list){

	for(int i = 0; i < list->size-1; i++)
		xchgNodes(list, atPos(list, i), min(list, i));
}

void dSort(List* list){

	for(int i = 0; i < list->size-1; i++)
		xchgNodes(list, atPos(list, i), max(list, i));
}



int main(){

	List* lista = createList();

	DataNode data;

	data.id = 5;
	push(lista, data);

	data.id = 4;
	push(lista, data);

	data.id = 3;
	push(lista, data);

	data.id = 2;
	push(lista, data);

	data.id = 1;
	push(lista, data);

	printList(lista);

	printf("****Testando função erase():****\n");

	erase(lista, 2);

	printList(lista);

	data.id = 3;
	insert(lista, data, 2);

	data.id = 6;
	insert(lista, data, 4);

	data.id = 7;
	insert(lista, data, 5);

	data.id = 8;
	insert(lista, data, 6);

	data.id = 9;
	insert(lista, data, 7);

	printList(lista);

	printf("Valor solicitado: %d\n", atPos(lista, 6)->data.id);

	printf("Index solicitado: %d\n", indexOf(lista, lista->head->next->next->next));


	printf("****Depois da inserção:****\n");
	printList(lista);


	xchgNodes(lista, lista->head->next->next->next->next,lista->head->next->next->next);

	printf("****Depois da troca de nó:****\n");

	printList(lista);

	printf("Valor mínimo a partir do índice: %d\n",min(lista, 3)->data.id);

	printf("Valor máximo a partir do índice: %d\n",max(lista, 1)->data.id);


	printf("****Testando função dSort():****\n");
	dSort(lista);
	printList(lista);

	printf("****Testando função cSort():****\n");
	cSort(lista);
	printList(lista);

	return 0;

}
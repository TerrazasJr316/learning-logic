#include <stdio.h>
#include <math.h>

void printnamaste();
void printbonjour();

int main() {
    char c;
    print("Ingresa: ");
    scanf("%c", &c);

    if (c == 'I') {
        print("namaste");
    }
    else {
        print("bonjour");
    }
}

void printnamaste() {
    print("namaste \n");
}
void printbonjour(){
    print("bonjour");
}
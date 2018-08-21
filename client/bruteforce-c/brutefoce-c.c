#include <stdio.h>
#include <string.h>
#include <stdbool.h>

const int checksum = 3696619;
const char *pass = "souris";
const char *alphabet = "                   azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789_$&#@";
int alphabet_length;
FILE *f;
const int login_nb_char = 6;
const int debut_alphabet = 19; // l'alphabet commence après 19 espaces
const char *nom_fichier = "epGameOver.txt";

int indexOf(char *lettre){
  char *b = strstr(alphabet, lettre);
  return b-alphabet;
}

int calculSum(char *login){
  int sum=1;
  char lettre[2];
	for (int i=0 ; i<login_nb_char ; i++) {
    strncpy(lettre, login+i, 1);
    lettre[1] = '\0';
		int index1=indexOf(lettre)+10;
    strncpy(lettre, pass+i, 1);
    lettre[1] = '\0';
		int index2=indexOf(lettre)+10;
		sum=sum+(index1*login_nb_char*(i+1))*(index2*(i+1)*(i+1));
	}
	return sum;
}

bool estCharInvalide(char c){
  // on enlève les char non valide pour une URL
  if(c == '#' || c == '&'){
    return true;
  }
  // d'après le forum, c'est que en minuscules...
  if(c >= 'a' && c <= 'z'){
    return false;
  }
  return true;
}

bool troisConsonnes(char *mot){
  int compteurConsonnes = 0;
  for(int i=0 ; i<strlen(mot) ; i++){
    char c = mot[i];
    if(c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'y'){
      compteurConsonnes++;
    } else {
      compteurConsonnes = 0;
    }
    if(compteurConsonnes >= 3){
      return true;
    }

  }
  return false;
}

void bruteforce(){
  char mot[7];
  for(int i6 = debut_alphabet; i6 < alphabet_length ; i6++) {
    if(estCharInvalide(alphabet[i6])){ continue; }
    for (int i5 = debut_alphabet; i5 < alphabet_length; i5++) {
      if(estCharInvalide(alphabet[i5])){ continue; }
  		for (int i4 = debut_alphabet; i4 < alphabet_length; i4++) {
        if(estCharInvalide(alphabet[i4])){ continue; }
  			for (int i3 = debut_alphabet; i3 < alphabet_length; i3++) {
          if(estCharInvalide(alphabet[i3])){ continue; }
  				for (int i2 = debut_alphabet; i2 < alphabet_length; i2++) {
            if(estCharInvalide(alphabet[i2])){ continue; }
  					for(int i1 = debut_alphabet; i1 < alphabet_length; i1++){
              if(estCharInvalide(alphabet[i1])){ continue; }
              snprintf(mot, sizeof mot, "%c%c%c%c%c%c", alphabet[i6], alphabet[i5], alphabet[i4],alphabet[i3],alphabet[i2],alphabet[i1]);
              // on enlève si 3 consonnes d'affilée
              if(troisConsonnes(mot)){
                continue;
              }
  						int sum = calculSum(mot);
  						if(sum == checksum){
  							printf("%s %d\n", mot, sum);
                fprintf(f, "%s\n", mot);
                fflush(f);
              }
  					}
  				}
  			}
  		}
  	}
    printf("avancement %.2f%%\n",(i6*100.0/alphabet_length));
  }
}

int main(void) {
  printf("hello world\n");
  // constantes
  f = fopen(nom_fichier, "w");
  alphabet_length = strlen(alphabet);
  // tests unitaires
  if(troisConsonnes("abc") || !troisConsonnes("afff")){
    printf("l'algo troisConsonnes est faux");
    return -2;
  }
  if(calculSum("aien3") != checksum){
    printf("l'algo calculSum est faux");
    return -1;
  }
  // BF
  bruteforce();
  printf("bye world\n");
  return 0;
}

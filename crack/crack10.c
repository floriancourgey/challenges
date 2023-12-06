#include <stdio.h>

int main() {
    // Assuming esi, ebp, and edi are variables or pointers defined elsewhere
    // in the code (not provided in the snippet).

    // Local variables
    int inputSerial;
    char inputName[108];
    int password;
    int i;

    // FUN_00402a30();
    // FUN_00401560();

    printf("Nom: ");
    inputName[0] = 'a';
    inputName[1] = 'd';
    inputName[2] = 'm';
    inputName[3] = 'i';
    inputName[4] = 'n';
    // fgets(inputName, 0x50, stdin);

    printf("Serial: ");
    // scanf("%u", &inputSerial);
    inputSerial = 449141;

    password = 0;
    i = 0;

    while (inputName[1] != '\0') {
        char salt = (char)(((int)(0x20a75279 / (unsigned int)inputName[i]) + i) % 5);
        password += ((unsigned int)inputName[1] * (unsigned int)inputName[i] % 0x20a75279) << salt;
        inputName[1] = inputName[i + 2];
        i += 1;
    }

    if (password == inputSerial) {
        puts("Serial correct");
    } else {
        puts("Serial incorrect");
    }

    getchar();
    getchar();

    return 0;
}

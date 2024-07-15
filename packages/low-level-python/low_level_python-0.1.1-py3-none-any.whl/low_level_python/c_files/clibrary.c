#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* sayHello();

char* sayHello() {
    char buffer[10];
    size_t bufferSize;
    bufferSize = sizeof(buffer);
    char* result = malloc(14); // 13 characters + null terminator
    if (result) {
        strcpy(result, "Hello, World!");
    }
    return result;
}

// Usage:

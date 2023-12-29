#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>

#define MAX_ARRAY_SIZE 100

int arr[MAX_ARRAY_SIZE];
int n;
int sorting_in_progress = 0;

void bubbleSort(int arr[], int n) {
    int temp, swapped;

    for (int i = 0; i < n - 1; i++) {
        swapped = 0;

        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1;
            }
        }

        if (swapped == 0) {
            break;
        }
    }

    sorting_in_progress = 0;
}

void startSorting(const char *input_text) {
    if (sorting_in_progress) {
        return;
    }

    sorting_in_progress = 1;

    int num;
    int count = 0;
    char input_text_copy[256];
    strcpy(input_text_copy, input_text);

    char *token = strtok(input_text_copy, " \t\n");

    while (token != NULL) {
        num = atoi(token);
        arr[count++] = num;
        token = strtok(NULL, " \t\n");
    }

    n = count;

    bubbleSort(arr, n);

    sorting_in_progress = 0;
}

void generateRandomValues() {
    srand(time(NULL));
    char random_values[256] = "";

    for (int i = 0; i < 10; i++) {
        if (i > 0) {
            strcat(random_values, " ");
        }
        int random_value = rand() % 100;
        char temp_value[16];
        sprintf(temp_value, "%d", random_value);
        strcat(random_values, temp_value);
    }

    startSorting(random_values);
}

void resetInput() {
    sorting_in_progress = 0;
    memset(arr, 0, sizeof(arr));
}

#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int items[20];
    int count;
} Array;


/**************************************
 * INPUT
 **************************************/

bool array_parse(Array *self) {
    for (int i = 0; i < self->count; ++i) {
        if (scanf("%d", self->items+i) == EOF) return false;
    }
    return true;
}


/**************************************
 * PROCESS
 **************************************/

int array_max(Array *self) {
    int m = self->items[0];
    for (int i = 1; i < self->count; ++i) {
        if (m < self->items[i]) m = self->items[i];
    }
    return m;
}

int array_sum(Array *self) {
    int sum = 0;
    for (int i = 0; i < self->count; ++i) {
        sum += self->items[i];
    }
    return sum;
}

/**************************************
 * OUTPUT
 **************************************/

void array_print(Array *self) {
    for (int i = 0; i < self->count; ++i) {
        printf("%d%c", self->items[i], (i == self->count-1) ? '\n' : ' ');
    }
}

void output(Array *out) {
    int sum = array_sum(out);

    printf("%d\n", sum);

    Array divisible = {.count=0};

    for(int i = 0; i < out->count; ++i) {
        if (sum % out->items[i] == 0) {
            divisible.items[divisible.count++] = out->items[i];
        }
    }

    if (divisible.count) {
        array_print(&divisible);
    } else {
        printf("-1\n");
    }
}


int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    
    Array out = {.count=n};
    Array in  = {.count=m};
    for (int i = 0; i < n; ++i) {
        array_parse(&in);
        out.items[i] = array_max(&in);
    }
    output(&out);
    return 0;
}

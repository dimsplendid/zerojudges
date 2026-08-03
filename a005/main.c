#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int items[5];
    int count;
} Array;

/**************************************
 * INPUT
 **************************************/

bool parse(Array *in) {
    for(int i = 0; i < in->count; ++i) {
        if (scanf("%d", &in->items[i]) == EOF) return false;
    }
    return true;
}

/**************************************
 * PROCESS
 **************************************/

typedef enum {
    AS, // 等差
    GS, // 等比
} Seq_Type;

typedef struct {
    Seq_Type type;
    int d;
} Seq_Info;

Seq_Info array_check(const Array *in) {
    if (in->items[1] - in->items[0] == in->items[2] - in->items[1]) {
        return (Seq_Info) {
            .type = AS,
            .d = in->items[1] - in->items[0],
        };
    } else {
        return (Seq_Info) {
            .type = GS,
            .d = in->items[1] / in->items[0]
        };
    }
}

void predict(const Array *in, Array *out) {
    for (int i = 0; i < in->count; ++i) {
        out->items[i] = in->items[i];
    }
    Seq_Info seq_info = array_check(in);
    switch (seq_info.type) {
        case AS: out->items[in->count] = in->items[in->count-1] + seq_info.d; break;
        case GS: out->items[in->count] = in->items[in->count-1] * seq_info.d; break;
    }
}

/**************************************
 * OUTPUT
 **************************************/

void array_print(Array *out) {
    for (int i = 0; i < out->count; ++i) {
        printf("%d%c", out->items[i], (i == out->count-1) ? '\n' : ' ');
    }
}

/**************************************
 * Entry Point
 **************************************/
int main(void) {

    int num_cases;
    if(scanf("%d", &num_cases) == EOF) return 0;
    // printf("%d\n", num_cases);
    Array in  = {.count=4};
    Array out = {.count=5};
    for(int i = 0; i < num_cases; ++i) {
        if (!parse(&in)) break;
        predict(&in, &out);
        // array_print(&in);
        array_print(&out);
    }
    
    return 0;
}

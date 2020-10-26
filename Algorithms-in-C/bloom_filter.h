#ifndef BLOOM_FILTER_H
#define BLOOM_FILTER_H

#include <stdbool.h>

typedef struct {
    int hash_count;
    int arr_len;
    bool *bit_array;
} bloom_filter_t;

bloom_filter_t *bloom_filter_create(
        int elem_count,
        float false_positive_probability);

void bloom_filter_add(bloom_filter_t *filter, char *s);

bool bloom_filter_might_contain(bloom_filter_t *filter, char *s);

void bloom_filter_destroy(bloom_filter_t *filter);

#endif

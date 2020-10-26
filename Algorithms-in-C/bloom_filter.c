#include "bloom_filter.h"

#include <stdint.h>
#include <stdlib.h>
#include <math.h>


uint64_t fnv(char *s)
{
    const uint64_t  MAGIC_PRIME = 0x00000100000001B3;
    uint64_t        hash        = 0xCBF29CE484222325;

    for (; *s; s++)
        hash = (hash ^ *s) * MAGIC_PRIME;

    return hash;
}

/*
 * Return the i'th hash of s between 0 and max.
 */
uint32_t hash(char *s, int i, int max) {
    // The following formula can be used to generate i hashes with just
    // two hash functions: (a + b * i) % m
    // For our purposes one hash function suffices because we can just split
    // the 64bit hash into two 32bit hashes.
    uint64_t hash = fnv(s);
    uint32_t a = (uint32_t)(hash & 0x00FFll);
    uint32_t b = (uint32_t)(hash & 0xFF00ll >> 32);
    return (a + b * i) % max;
}

int max(int a, int b) {
    if (a > b) return a;
    return b;
}

/*
 * Calculate the optimal number of hash functions from the expected number of
 * insertions and the expected bits per insertions.
 */
int _optimal_num_of_hash_functions(int n, long bpi) {
    return max(1, (int)round(bpi / n * log(2)));
}

int _optimal_num_of_bits(int n, float p) {
    return (int)(-n * log(p) / (log(2) * log(2)));
}

bloom_filter_t *bloom_filter_create(int elem_count,
                                    float false_positive_probability) {
    bloom_filter_t *filter;
    int num_of_bits = _optimal_num_of_bits(elem_count, false_positive_probability);
    filter = malloc(sizeof(bloom_filter_t));
    filter->arr_len = num_of_bits;
    filter->bit_array = calloc(1, filter->arr_len);

    int bits_per_insertion = elem_count / num_of_bits;
    int num_of_hashes = _optimal_num_of_hash_functions(elem_count, bits_per_insertion);
    filter->hash_count = num_of_hashes;
    return filter;
}

void bloom_filter_add(bloom_filter_t *filter, char *s) {
    for (int i = 1; i <= filter->hash_count; i++) {
        filter->bit_array[hash(s, i, filter->arr_len)] = true;
    }
}

bool bloom_filter_might_contain(bloom_filter_t *filter, char *s) {
    for (int i = 1; i <= filter->hash_count; i++) {
        if (!filter->bit_array[hash(s, i, filter->arr_len)])
            return false;
    }
    return true;
}

void bloom_filter_destroy(bloom_filter_t *filter) {
    free(filter->bit_array);
    free(filter);
}

#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H

#include <stdint.h>

typedef enum {
    BLACK = 0, BROWN, RED, ORANGE, YELLOW,
    GREEN, BLUE, VIOLET, GREY, WHITE
} resistor_band_t;

typedef enum {
    OHMS,
    KILOOHMS,
    MEGAOHMS,
    GIGAOHMS
} unit_t;

typedef struct {
    uint16_t value;
    unit_t unit;
} resistor_value_t;

/**
 * This function takes a pointer to an array of resistor_band_t elements
 * and returns a resistor_value_t struct containing the resistor value and its unit.
 */
resistor_value_t color_code(const resistor_band_t *colors);

#endif

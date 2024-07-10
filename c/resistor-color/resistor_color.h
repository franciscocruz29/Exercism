#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H
#include <inttypes.h>

typedef enum resistor_band
{
    BLACK, BROWN, RED, ORANGE, YELLOW,
    GREEN, BLUE, VIOLET, GREY, WHITE
} resistor_band_t;

// Returns the unsigned integer value corresponding to the given color
uint16_t color_code(resistor_band_t color);

// Returns the address of an array containing resistor band color codes
const resistor_band_t* colors(void);

#endif

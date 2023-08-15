// 1. Understand the Problem
// - What is the input?
// - String -- a message to encode or decode

// - What is the output?
// - String -- the encoded or decoded message

// - What are the requirements?
// - Implement a simple shift cipher like the Caesar Cipher
// A shift cipher involves replacing each letter in the message by a letter that
// is some fixed number of positions further along in the alphabet.
// We’ll call this number the encryption key. It is just the length of the shift we are using.
// The encryption key must be between 1 and 25.

// - Must be able to encode and decode messages

// 2. Examples

// Giving "iamapandabear" as input to the encode function returns the cipher "ldpdsdqgdehdu". Obscure enough to keep our message secret in transit.
// When "ldpdsdqgdehdu" is put into the decode function it would return the original "iamapandabear"

// 3. Algorithm

// 1. Cipher Class Initialization:
// The Cipher class is initialized with an optional key. If no key is provided, a random key of 100 lowercase letters is generated.
// If a key is provided, it is validated to ensure it contains only lowercase letters.

// 2. Encoding:

// To encode a message:
// Iterate through each character in the message:
// Convert the character to its corresponding numerical value(0 - 25) by subtracting the ASCII value of 'a'(97).
// Obtain the shift value by taking the numerical value of the key character at the current position in the key(looping back to the beginning of the key if necessary).
// Add the shift value to the character's numerical value.
// Take the result modulo 26 to ensure it wraps around the alphabet.
// Convert the resulting numerical value back to a character by adding the ASCII value of 'a'.
// Append the encoded character to the encoded message.

// 3. Decoding:

// To decode an encoded message:
// Iterate through each character in the encoded message:
// Convert the character to its corresponding numerical value(0 - 25) by subtracting the ASCII value of 'a'(97).
// Obtain the shift value by taking the numerical value of the key character at the current position in the key(looping back to the beginning of the key if necessary).
// Subtract the shift value from the character's numerical value.
// Add 26 to the result to ensure it wraps around the alphabet correctly.
// Take the result modulo 26 to obtain the original numerical value.
// Convert the resulting numerical value back to a character by adding the ASCII value of 'a'.
// Append the decoded character to the decoded message.

// 4. Random Key Generation:

// To generate a random key:
// Generate a sequence of 100 lowercase letters by:
// Iterating 100 times:
// Generate a random number between 0 and 25(inclusive) to represent a lowercase letter.
// Convert the random number to a character by adding the ASCII value of 'a'.
// Append the character to the key.

// 5. Key Validation:

// To validate a key:
// Check if the key contains only lowercase letters(a - z) using a regular expression.
// If the key is not valid, throw an error indicating that the key must contain only lowercase letters.


export class Cipher {
  constructor(key) {
    if (!key) {
      this.key = this.generateRandomKey();
    } else {
      this.validateKey(key);
      this.key = key;
    }
  }

  generateRandomKey() {
    let key = '';
    for (let i = 0; i < 100; i++) {
      const randomCharCode = Math.floor(Math.random() * 26) + 97; // Random lowercase letter
      key += String.fromCharCode(randomCharCode);
    }
    return key;
  }

  validateKey(key) {
    if (!/^[a-z]+$/.test(key)) {
      throw new Error('Key must contain only lowercase letters.');
    }
  }

  encode(message) {
    let encoded = '';
    for (let i = 0; i < message.length; i++) {
      const charCode = message.charCodeAt(i) - 97;
      const shift = this.key.charCodeAt(i % this.key.length) - 97;
      const encodedCharCode = (charCode + shift) % 26 + 97;
      encoded += String.fromCharCode(encodedCharCode);
    }
    return encoded;
  }

  decode(encoded) {
    let decoded = '';
    for (let i = 0; i < encoded.length; i++) {
      const charCode = encoded.charCodeAt(i) - 97;
      const shift = this.key.charCodeAt(i % this.key.length) - 97;
      const decodedCharCode = (charCode - shift + 26) % 26 + 97;
      decoded += String.fromCharCode(decodedCharCode);
    }
    return decoded;
  }
}

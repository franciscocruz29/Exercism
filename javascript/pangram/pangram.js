export const isPangram = (sentence) => {
  return new Set(sentence.toLowerCase().match(/[a-z]/g)).size === 26;
};

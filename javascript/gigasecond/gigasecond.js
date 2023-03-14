
export const gigasecond = (internalDate) => {
  return new Date(internalDate.getTime() + 10 ** 12);
};

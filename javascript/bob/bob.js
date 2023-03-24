export const hey = (message) => {
  const trimmedMessage = message.trim();
  if (!trimmedMessage) {
    return "Fine. Be that way!";
  }
  const isYelling =
    trimmedMessage === trimmedMessage.toUpperCase() &&
    /[A-Z]+/.test(trimmedMessage);
  const isQuestion = trimmedMessage.endsWith("?");

  if (isYelling) {
    return isQuestion ? "Calm down, I know what I'm doing!" : "Whoa, chill out!";
  };
  if (isQuestion) {
    return "Sure.";
  };
  return "Whatever.";
};

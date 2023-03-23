export function hey(message: string): string {
  message = message.trim();
  if (!message) {
    return "Fine. Be that way!";
  }
  const isYelling = message === message.toUpperCase() && /[A-Z]+/.test(message);
  const isQuestion = message.endsWith("?");
  if (isYelling && isQuestion) {
    return "Calm down, I know what I'm doing!";
  }
  if (isYelling) {
    return "Whoa, chill out!";
  }
  if (isQuestion) {
    return "Sure.";
  }
  return "Whatever.";
}

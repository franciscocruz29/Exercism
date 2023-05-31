/* 
Constructor: The constructor takes in hours and minutes, converts them to total minutes, and then uses modulus to get the equivalent minute within a day. 
If the total minutes is negative, it adds 24*60 to get the positive equivalent. It then calculates the actual hour and minute by dividing total minutes by 60.

toString: This method converts the hour and minute to string, ensuring they are always two digits long, and returns the time in the format 'HH:MM'.

plus: This method adds the given minutes to the current time and creates a new Clock instance with the updated time. The constructor of the Clock class will handle the overflow or underflow of hours and minutes.

minus: This method subtracts the given minutes from the current time and creates a new Clock instance with the updated time.

equals: This method compares the hour and minute of the current Clock instance with another one. It returns true if they are the same, and false otherwise. */

export class Clock {
  private hour: number;
  private minute: number;

  constructor(hour: number, minute: number = 0) {
    // Convert the hours and minutes to total minutes
    let totalMinutes = hour * 60 + minute;

    // Use modulus to get the equivalent minute within a day (24*60 minutes)
    // If the total minutes is negative, add 24*60 to get the positive equivalent
    totalMinutes = totalMinutes % (24 * 60);
    if (totalMinutes < 0) totalMinutes += 24 * 60;

    // Calculate the actual hour and minute by dividing total minutes by 60
    this.hour = Math.floor(totalMinutes / 60);
    this.minute = totalMinutes % 60;
  }

  public toString(): string {
    // Convert the hour and minute to string
    // Use padStart to ensure they are always two digits long
    // Return the time in the format 'HH:MM'
    let hourString = this.hour.toString().padStart(2, "0");
    let minuteString = this.minute.toString().padStart(2, "0");
    return `${hourString}:${minuteString}`;
  }

  public plus(minutes: number): Clock {
    // Add the given minutes to the current time
    // Create a new Clock instance with the updated time
    // The constructor of the Clock class will handle the overflow or underflow of hours and minutes.
    return new Clock(this.hour, this.minute + minutes);
  }

  public minus(minutes: number): Clock {
    // Subtract the given minutes from the current time
    // Create a new Clock instance with the updated time
    return new Clock(this.hour, this.minute - minutes);
  }

  public equals(other: Clock): boolean {
    // Compare the hour and minute of the current Clock instance with the other
    // Return true if they are the same, false otherwise
    return this.hour === other.hour && this.minute === other.minute;
  }
}

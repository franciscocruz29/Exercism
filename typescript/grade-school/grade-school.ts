// This code defines a simple grade school system where you can add students, retrieve the roster of students, and get students by their grade.

interface Student {
  name: string;
  grade: number;
}

export class GradeSchool {
  private students: Student[] = []; // It will store Student objects

  // This method returns a roster of students, sorted by grade and then by name
  roster(): Record<number, string[]> {
    const result: Record<number, string[]> = {};

    this.students.forEach(({ grade, name }) => {
      result[grade] = result[grade] || []; // If a grade does not already exist in the result object, an empty array is assigned to that key
      result[grade].push(name);
    });

    for (const key in result) {
      result[Number(key)].sort(); // Sort the names of the students in each grade in alphabetical order
    }

    return result;
  }

  add(name: string, grade: number): void {
    this.students = this.students.filter((student) => student.name !== name);
    this.students.push({ name, grade });

    // if two students have the same grade, their names are compared in a locale-sensitive manner
    // if their grades are different, they are sorted by grade
    this.students.sort((a, b) =>
      a.grade === b.grade ? a.name.localeCompare(b.name) : a.grade - b.grade
    );
  }

  // This method returns an array of students names that belong to a specific grade, sorted alphabetically
  grade(grade: number): string[] {
    return this.students
      .filter(({ grade: studentGrade }) => studentGrade === grade)
      .map(({ name }) => name)
      .sort();
  }
}

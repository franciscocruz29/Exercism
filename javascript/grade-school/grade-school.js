// This code defines a simple grade school system where you can add students,
// retrieve the roster of students, and get students by their grade.
export class GradeSchool {
  constructor() {
    this.students = [];
  }

  // This method returns a roster of students, sorted by grade and then by name.
  // It first iterates through the list of students, adding each student's name
  // to an array associated with their grade. Then, it sorts the names of the students
  // in each grade in alphabetical order before returning the entire roster.
  roster() {
    const result = {};

    this.students.forEach(({ grade, name }) => {
      result[grade] = result[grade] || [];
      result[grade].push(name);
    });

    for (const key in result) {
      result[Number(key)].sort();
    }

    return result;
  }

  // This method adds a new student to the list of students.
  // If a student with the same name already exists in the list, the old entry
  // is removed and replaced with the new entry. Students are then sorted by grade
  // and by name in alphabetical order.
  add(name, grade) {
    this.students = this.students.filter((student) => student.name !== name);

    this.students.push({ name, grade });

    this.students.sort((a, b) =>
      a.grade === b.grade ? a.name.localeCompare(b.name) : a.grade - b.grade
    );
  }

  // This method returns an array of students' names that belong to a specific
  // grade, sorted alphabetically. It filters the list of students, selecting
  // only those with the specified grade, and then maps the resulting list to
  // include only the students' names before sorting the names alphabetically.
  grade(grade) {
    return this.students
      .filter(({ grade: studentGrade }) => studentGrade === grade)
      .map(({ name }) => name)
      .sort();
  }
}


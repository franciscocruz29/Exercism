
export class Matrix {
  constructor(string) {
    this.string = string;
  }

  static parseRows(string) {
    return string.split('\n').map(row => row.split(' ').map(Number));
  }

  static transpose(rows) {
    return rows[0].map((_, i) => rows.map(row => row[i]));
  }

  get rows() {
    return Matrix.parseRows(this.string);
  }

  get columns() {
    return Matrix.transpose(this.rows);
  }
}

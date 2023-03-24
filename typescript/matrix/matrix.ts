export class Matrix {
  private stringMatrix: string;

  constructor(stringMatrix: string) {
    this.stringMatrix = stringMatrix;
  }

  get rows(): number[][] {
    return this.stringMatrix.split("\n").map((row) => row.split(" ").map(Number));
  }

  get columns(): number[][] { 
    return this.rows[0].map((_, index) => this.rows.map((row) => row[index]));
  }
}

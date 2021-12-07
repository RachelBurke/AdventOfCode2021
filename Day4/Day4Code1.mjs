import { readFileSync } from "fs";

// Read the file input
const input = readFileSync("./Day4Input.txt").toString("utf-8").trim().split("\r\n");

// Get the numbers drawn
let numbersDrawn = input.slice(0).toString().split(",").map(i => parseInt(i));

// Handle creating all the bingo boards as an array of objects { rows: [Array], columns: [Array]}
function createBoards(boardList) {
    const boards = [];
    let columns = [[],[],[],[],[]];
    let board = { rows: [], columns: [] };

    boardList.map((r, i) => {
        // when reading empty line we need to initialize a new board
        if(r == ''){
            if(i != 0){
                board.columns = columns;
                boards.push(board);
            }

            columns = [[],[],[],[],[]];
            board = { rows: [], columns: [] };
        } else {
            let row = r.trim().split(/\s/g).filter(x => x).map(x => parseInt(x));

            board.rows.push(row);
            row.forEach((cell, i) => columns[i].push(cell));
        }

    })

    return boards;
}

const boards = createBoards(input.slice(1));

let hasWon = false;
let score;

for (let n = 0; n < numbersDrawn.length; n++) {
    const number = numbersDrawn[n];

    for (let b = 0; b < boards.length; b++) {
        const board = boards[b];
    
        for (let r = 0; r < board.rows.length; r++) {
            const row = board.rows[r];

            if(row.includes(number)) {
                row[row.findIndex(x => x == number)] = 0;
            }

            if(row.reduce((x,y) => x + y) == 0){
                hasWon = true;
                break;
            }          
        }

        for (let c = 0; c < board.columns.length; c++) {
            const column = board.columns[c];

            if(column.includes(number)) {
                column[column.findIndex(x => x == column)] = 0;
            }

            if(column.reduce((x,y) => x + y) == 0){
                hasWon = true;
                break;
            } 
        }

        if(hasWon){
            let sum = 0;
            board.rows.forEach(row => sum += row.reduce((x,y) => x + y));
            score = sum * numbersDrawn[n];
            break;
        }     
    }
    
    if(hasWon) {
        break;
    }
}

console.log(score); //31424


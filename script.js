const boardElement = document.getElementById('board');

const initialSetup = [
    ['香','桂','銀','金','王','金','銀','桂','香'],
    ['','飛','','','','','','角',''],
    ['歩','歩','歩','歩','歩','歩','歩','歩','歩'],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['歩','歩','歩','歩','歩','歩','歩','歩','歩'],
    ['','角','','','','','','飛',''],
    ['香','桂','銀','金','玉','金','銀','桂','香']
];

const boardState = [];
let selected = null;

function renderBoard() {
    boardElement.innerHTML = '';
    for (let y = 0; y < 9; y++) {
        for (let x = 0; x < 9; x++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.dataset.x = x;
            cell.dataset.y = y;
            cell.textContent = boardState[y][x];
            cell.addEventListener('click', onCellClick);
            boardElement.appendChild(cell);
        }
    }
}

function onCellClick(e) {
    const x = parseInt(e.target.dataset.x);
    const y = parseInt(e.target.dataset.y);
    if (selected) {
        boardState[y][x] = boardState[selected.y][selected.x];
        boardState[selected.y][selected.x] = '';
        selected = null;
        renderBoard();
    } else if (boardState[y][x]) {
        selected = {x, y};
        e.target.classList.add('selected');
    }
}

function init() {
    for (let row of initialSetup) {
        boardState.push([...row]);
    }
    renderBoard();
}

init();

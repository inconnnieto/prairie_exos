import namelist from './4_Exo_Quarta.json' assert {type: 'json'};

function groupes(k) {
    if (k < 1) { throw new Error("nope"); }
    let l = [...namelist];
    l.sort((a, b) => Math.random() - 0.5);
    let result = [];
    while (l.length > 0) {
        result.push(l.splice(0, k));
    }
    return result;
}

const k = 4;
console.log(groupes(k));
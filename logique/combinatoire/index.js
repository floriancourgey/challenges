function combinatoire(inputs){
    var a = inputs[0] == '1';
    var b = inputs[1] == '1';
    var c = inputs[2] == '1';
    var d = inputs[3] == '1';
    var e = inputs[4] == '1';

    var gate1_AND = a && b;
    var gate1_NXOR = !(c ^ d);
    var gate1_OR = e || e;

    var gate2_NOR = !(gate1_NXOR || gate1_OR);

    var gate3_XOR = gate1_AND ^ gate2_NOR;

    var gate4_NAND = !(gate3_XOR && e);

    var gate5_NAND = !( !gate3_XOR && (!(!(!gate4_NAND))) );

    var gate6_XOR = gate5_NAND ^ (!(!(!(!gate4_NAND))));

    return gate6_XOR;
}

var goodBoys = [];
for (let i = 0; i < 32; i++) { // 2^5 = 32, counting from 0 to 31
    let binaryRepresentation = i.toString(2).padStart(5, '0');
    let s = combinatoire(binaryRepresentation);
    console.log(`Input: ${binaryRepresentation}, S: ${s}`);
    if(s){
        goodBoys.push(binaryRepresentation);
    }
}
console.log(goodBoys.length+' solutions:\n'+goodBoys.join('-'));
const demo= ["nemo"];
const demo2=["semo", "remo", "femo","aemo", "leno","dro", "gemo","brk", "jb","kdbj","sf","nemo"];
const large = new Array(100000000).fill("semo");

function findNemo(array){
    let t0 = performance.now();

    for(let i=0;i<array.length;i++){
       
        if(array[i]==="nemo"){
            console.log("Found Nemo!");
        }
    }
    let t1 = performance.now();
    console.log("Time taken = "+(t1-t0)+" milliseconds");

}

findNemo(large);

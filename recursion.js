const count=(n)=> {
    console.log(n);
    return count(n - 1);
};

count(101);
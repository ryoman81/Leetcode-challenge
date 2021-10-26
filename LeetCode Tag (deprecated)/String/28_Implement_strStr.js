var strStr = function(haystack, needle) {
    
    for (let i = 0; i < haystack.length-needle.length+1; i++) {
        let h = 0;
        let n = 0;
        while (n < needle.length) {
            if (haystack[i+h] !== needle[n]) break;
            n++; h++;
        }
        if (n === needle.length)
            return i;
    }
    
    return -1;
    
};

const reuslt = strStr("hello", "ll");
console.log(reuslt);
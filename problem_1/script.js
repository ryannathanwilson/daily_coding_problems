function hasSumK(arr, k) {
    hashMap = {};
    for (let value of arr) {
        if (hashMap[value]) { 
            return true;
        } else { 
            hashMap[k - value] = true 
        };
    }
    return false;
}
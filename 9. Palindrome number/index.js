/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) {
        return false;
    }
    let str = x.toString();
    const reverseStr = str.split('').reverse().join('');
    return str === reverseStr;
};
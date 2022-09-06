// Lab 01, Algorithm analysis
// Task: calculate Levenshtein distance - non-recurcive algorithm,
// calculate Domerau-Levenshtein distance - non-recurcive,
// recursive algorithm without cache, with cache

function levenshteinDistance(str1, str2) {
    if (str1.length < str2.length) {
        [str1, str2] = [str2, str1];
    }

    let previousRow = Array(str2.length + 1);
    let currentRow = Array(str2.length + 1);

    for (let i = 0; i < str1.length + 1; i++) {
        for (let j = 0; j < str2.length + 1; j++) {
            if (i === 0 && j === 0) {
                currentRow[j] = 0;
            } else if (i > 0 && j === 0) {
                currentRow[j] = i;
            } else if (i === 0 && j > 0) {
                currentRow[j] = j;
            } else {
                currentRow[j] = Math.min(
                    currentRow[j - 1] + 1,
                    previousRow[j] + 1,
                    previousRow[j - 1] + (str1[i - 1] === str2[j - 1] ? 0 : 1)
                );
            }
        }
        previousRow = [...currentRow];
    }
    return currentRow[str2.length];
}

module.exports = levenshteinDistance;
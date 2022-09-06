let levenshteinDistance = require("./levenshteinDistance");

describe("Levenshtein distance search, non-recurcive", function () {
    let testCases = [
        {
            firstWord: "",
            secondWord: "",
            result: 0,
        },
        {
            firstWord: "",
            secondWord: "кот",
            result: 3,
        },
        {
            firstWord: "кот",
            secondWord: "скат",
            result: 2,
        },
        {
            firstWord: "скат",
            secondWord: "кот",
            result: 2,
        },
        {
            firstWord: "кот",
            secondWord: "кот",
            result: 0,
        },
    ];
    testCases.forEach(suit => {
        test(`${suit.firstWord} to ${suit.secondWord}`, () => {
            expect(levenshteinDistance(suit.firstWord, suit.secondWord))
            .toBe(suit.result);
        });
    });
});

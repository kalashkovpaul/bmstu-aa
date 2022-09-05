let levDistance = require("./levenshteinDistance");

test("кот to скат", function () {
    expect(levenshteinDistance("кот", "скат")).toBe(2);
});

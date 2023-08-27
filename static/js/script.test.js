/**
 * @jest-environment jsdom
 */

const addNewForm = require("./script.js");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

describe("add exercise button adds new form", () => {
    
    test("expects total number of exercise-form divs to be 4", () => {
        document.getElementById('add-form').click();
        
        expect($('.exercise-form').length).toBe(4);
    });
});


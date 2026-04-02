// not bad
// 1. Create the sentence variable
let sentence = "The movie is not that bad, I like it";

// 2. Find the position of the word "not"
let wordNot = sentence.indexOf("not");

// 3. Find the position of the word "bad"
let wordBad = sentence.indexOf("bad");

// 4. Check the conditions
// We check if "not" exists, "bad" exists, and if "bad" comes after "not"
if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    
    // Slice out the part from 'not' to 'bad' (+3 to include the word 'bad')
    // We replace that chunk with "good"
    let beforeNot = sentence.slice(0, wordNot);
    let afterBad = sentence.slice(wordBad + 3);
    
    console.log(beforeNot + "good" + afterBad);
    
} else {
    // If conditions aren't met, log the original sentence
    console.log(sentence);
}
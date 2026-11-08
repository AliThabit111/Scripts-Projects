// Number Guessing Game (Node.js): guess the secret number between 1 and 20.
import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const LOW = 1;
const HIGH = 20;

const rl = readline.createInterface({ input, output });

try {
    const secret = Math.floor(Math.random() * HIGH) + LOW;
    let tries = 0;
    let guess = null;

    console.log(`I'm thinking of a number between ${LOW} and ${HIGH}`);

    while (guess !== secret) {
        const text = await rl.question("Take a guess: ");
        guess = Number.parseInt(text, 10);

        if (Number.isNaN(guess)) {
            console.log("Please enter a whole number.");
            continue;
        }

        tries += 1;

        if (guess < LOW || guess > HIGH) {
            console.log("That number is out of range. Try again.");
        } else if (guess < secret) {
            console.log("Too low, try again.");
        } else if (guess > secret) {
            console.log("Too high, try again.");
        } else {
            console.log("You got it in", tries, "tries!");
        }
    }
} finally {
    rl.close();
}

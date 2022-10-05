const seconds = new Date().getTime() / 1000;

setTimeout(() => {
  // prints out "2", meaning that the callback is not called immediately after 500 milliseconds.
  console.log(`Ran after ${new Date().getTime() / 1000 - seconds} seconds`);
}, 500)

while (true) {
  if (new Date().getTime() / 1000 - seconds >= 10) {
    console.log("Good, looped for 10 seconds");
    break;
  }
}
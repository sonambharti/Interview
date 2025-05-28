console.log('Start');

setTimeout(() => {
  console.log('Timeout');
}, 0);

Promise.resolve().then(() => {
  console.log('Promise');
});

console.log('End');

/**
Output:
Start
End
Promise
Timeout

🔍 Step-by-step Execution
1. console.log('Start');
This is a synchronous operation.

Output: Start

2. setTimeout(..., 0)
This is an asynchronous operation using a macro-task (from the task queue).

It is scheduled to run after 0 ms, but it doesn’t execute immediately — it waits for the current call stack and microtasks to finish.

3. Promise.resolve().then(...)
This is a micro-task (goes to the microtask queue).

It is scheduled to execute after the current call stack but before any macro-tasks.

4. console.log('End');
This is synchronous.

Output: End
*/

// Predic the value of count at 1st onClick event on button.

import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
    setCount(count + 1);
  };

  return (
    <div>
      <p>{count}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
}

/**
on 1st event the value of count will be 1, although we are calling setCount twice in same handleClick function.
As, setCount is updating the old value again and again.

To call setCount on updated count to get count=2, code is:
setCount((count) => count + 1};
*/

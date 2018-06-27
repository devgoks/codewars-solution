snail = function(array) {
    var result;
  while (array.length) {
    // gets the first row.
    result = (result ? result.concat(array.shift()) : array.shift());
    // gets the right column.
    for (var i = 0; i < array.length; i++)
      result.push(array[i].pop());
    // gets the bottom row.
    result = result.concat((array.pop() || []).reverse());
    // gets the left column.
    for (var i = array.length - 1; i >= 0; i--)
      result.push(array[i].shift());
  }
  return result;
}
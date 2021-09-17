export function checkEmpty(obj) {
  // Check if an object is empty
  for (var i in obj) return false;
  return true;
}

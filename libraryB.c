// libcstar procedures for printing
void init_library();
void print(uint64_t* s);
void print_integer(uint64_t n);

uint64_t add_libraryB(uint64_t a, uint64_t b) {
    return 4*a + 4*b;
}

uint64_t main() {
  uint64_t result;

  // initialize selfie's libcstar library
  init_library();

  result = add_libraryB(2,2);
  
  print("Result: ");
  print_integer(result);

  // set i to its most recent value before it became 0
  return result;

}

void println();
void init_library();
void print(uint64_t* s);
void printf3(char* s, char* a1, char* a2, char* a3);

uint64_t main() {
  uint64_t i;
  uint64_t j;
  uint64_t u;

  // initialize selfie's libcstar library
  init_library();

  

  // print u in binary
  printf2("%s: usage: selfie [ %s ]\n", "-c { source } | -o binary | [ -s | -S ] assembly | -l binary | -sat dimacs | -i ",
    "( -m | -d | -r | -y | -min | -mob | -se | -mc ) 0-4096 ... ");
}

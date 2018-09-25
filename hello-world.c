  #include "hammer/src/hammer.h"
  #include <stdio.h>

  int main(int argc, char *argv[]) {
      uint8_t input[1024];
      size_t inputsize;

      HParser *hello_parser = h_token("Hello World", 11);

      inputsize = fread(input, 1, sizeof(input), stdin);

      HParseResult *result = h_parse(hello_parser, input, inputsize);
      if(result) {
          printf("yay!\n");
      } else {
          printf("boo!\n");
      }
  }

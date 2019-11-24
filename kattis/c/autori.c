#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) 
{
	char *input;
	char *result, *rs;
	input = malloc(256); //don't read more than 255 chars.
	rs = result = malloc(50); //don't read more than 50 chars.
	scanf("%s", input);
	char *token = strtok(input,"-");
	while(token) {
		*result++ = token[0];
		token= strtok(NULL, "-");
	}
	*result++ = '\0';
	printf("%s",rs);
	printf("result: %u\n",strlen(rs));
	free(rs);
	return 0;
}
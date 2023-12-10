ORG 1000H

FACT MACRO NUM
    MOV CH, NUM 
    MOV AX, 01H
    L1:
        MUL CH
        DEC CH
        JNZ L1 
ENDM  

MOV CL, 04H 
 
FACT CL
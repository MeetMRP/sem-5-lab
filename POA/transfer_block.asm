ORG 1000H

MOV CL, 04H
MOV SI, 1000H     
MOV DI, 6000H

MOVE:
    MOV CH, CL
    MOV AL, [SI]
    MOV BL, [DI]
    
    MOV [DI], AL
    MOV [SI], BL
    
    INC SI
    INC DI
    DEC CL
    JNZ MOVE
rel 
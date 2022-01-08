# SAA7706_RE

Reverse engineering notes and I2C samples of the SAA7706 DSP IC. Found in SAAB 9-3II head units.



# Register Access Frequency

# Reads

| ADDR | Name        | Count |
| ---- | ----------- | ----- |
| 0x07 | XRAM (DSP1) | 2225  |
| 0x22 | XRAM (DSP1) | 2222  |



Mysterious 0x45 addres... maybe radio?



# Writes

| ADDR              | Name                                          | Count  |
| ----------------- | --------------------------------------------- | ------ |
| 0x0F,0xFF         | DSP CONTROL                                   | 2      |
| 0x1F,0xF0         | Evaluation register                           | 1      |
| 0x1F,0xF3         | CL_GEN reg 1                                  | 1      |
| 0x1F,0xF4         | CL_GEN reg 2                                  | 1      |
| 0x1F,0xF6         | CL_GEN reg 4                                  | 1      |
| 0x1F,0xF7         | Selector register                             | 1      |
| 0x1F,0xF8         | IAC settings register (ignition interferance) | 3      |
| 0x1F,0xF9         | Clock settings register                       | 2      |
| 0x1F,0xFA         | Clock coefficient register                    | 1      |
| 0x1F,0xFB         | FMD and RDS sensitivity                       | 2      |
| 0x1F,0xFC         | Phone, nav, and audio register                | 1      |
| 0x1F,0xFD         | I/O config for DSP2                           | 1      |
| 0x08,0x00         | YRAM (DSP1)                                   | 1      |
| 0x10,0x00         | XRAM (DSP2)                                   | 1      |
| 0x21,0x2          | YRAM (DSP2)                                   | 7      |
| 0x11,0x3E to 0xFD | XRAM (DSP2) (this looks like an equaliser)    | 166    |
| 0x20XX or 0x21XX  | YRAM (DSP2) (this looks like an equaliser)    | 128+28 |
|                   |                                               |        |
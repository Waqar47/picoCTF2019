#!/bin/bash

#assuming only 1000.tar is downloaded

tar -xf 1000.tar #deflates to 999.tar

#then
for file in {999,1};do tar -xf '$file.tar' && rm '$file.tar'

#flag.png will be extracted after defalting 1.tar
